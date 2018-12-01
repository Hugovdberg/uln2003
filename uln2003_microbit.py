import microbit
from uln2003 import *
# (c) IDWizard 2017
# MIT License.

microbit.display.off()


class Stepper(StepperBase):
    def _set_pin(self, pin, value):
        self.pins[pin].write_digital(value)

    def _wait(self):
        microbit.sleep(self.delay)


if __name__ == '__main__':
    FULL_ROTATION = 4096
    s1 = Stepper(HALF_STEP, microbit.pin16, microbit.pin15,
                 microbit.pin14, microbit.pin13, delay=5)
    s2 = Stepper(HALF_STEP, microbit.pin6, microbit.pin5,
                 microbit.pin4, microbit.pin3, delay=5)
    # s1.step(FULL_ROTATION)
    # s2.step(FULL_ROTATION)

    runner = Driver()
    runner.run([Command(s1, FULL_ROTATION, 1),
                Command(s2, FULL_ROTATION/2, -1)])
