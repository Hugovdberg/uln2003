# (c) IDWizard 2017
# MIT License.

LOW = const(0)
HIGH = const(1)

HALF_STEP = [
    [LOW, LOW, LOW, HIGH],
    [LOW, LOW, HIGH, HIGH],
    [LOW, LOW, HIGH, LOW],
    [LOW, HIGH, HIGH, LOW],
    [LOW, HIGH, LOW, LOW],
    [HIGH, HIGH, LOW, LOW],
    [HIGH, LOW, LOW, LOW],
    [HIGH, LOW, LOW, HIGH],
]

FULL_STEP = [
    [HIGH, LOW, HIGH, LOW],
    [LOW, HIGH, HIGH, LOW],
    [LOW, HIGH, LOW, HIGH],
    [HIGH, LOW, LOW, HIGH]
]

WAVE_STEP = [
    [HIGH, LOW, LOW, LOW],
    [LOW, HIGH, LOW, LOW],
    [LOW, LOW, HIGH, LOW],
    [LOW, LOW, LOW, HIGH]
]


class Command():
    """Tell a stepper to move X many steps in direction"""

    def __init__(self, stepper, steps, direction=1):
        self.stepper = stepper
        self.steps = steps
        self.direction = direction


class Driver():
    """Drive a set of motors, each with their own commands"""

    @staticmethod
    def run(commands):
        """Takes a list of commands and interleaves their step calls"""

        # Work out total steps to take
        max_steps = sum([c.steps for c in commands])

        count = 0
        while count != max_steps:
            for command in commands:
                # we want to interleave the commands
                if command.steps > 0:
                    command.stepper.step(1, command.direction)
                    command.steps -= 1
                    count += 1


class StepperBase():
    """Base class to define Stepper classes for different boards."""

    def __init__(self, mode, pin1, pin2, pin3, pin4, delay=2):
        self.mode = mode
        self.pins = [pin1, pin2, pin3, pin4]
        self.delay = delay  # Recommend 10+ for FULL_STEP, 1 is OK for HALF_STEP
        self.current_step = 0

        # Initialize all to 0
        self.reset()

    def _set_pin(self, pin, value):
        pass

    def _wait(self):
        pass

    def step(self, count, direction=1):
        """
        step Rotate the stepper motor

        Rotates the motor by the number of steps given. The size of the step is
        determined by the motor itself and the selected mode.

        Args:
            count (int): Number of steps to move, if negative in the opposite
                direction of the given direction (-1 step backward == 1 forward).
            direction (int, optional): Defaults to 1. Direction to move, either
                1 for forwards, or -1 for backwards.
        """

        if count < 0:
            direction = -direction
            count = -count
        for _ in range(count):
            self.current_step += direction
            bit = self.mode[self.current_step % len(self.mode)]
            for p, v in enumerate(bit):
                self._set_pin(p, v)
            self._wait()
        self.reset()

    def reset(self):
        # Reset to 0, no holding, these are geared, you can't move them
        for p in range(4):
            self._set_pin(p, 0)
