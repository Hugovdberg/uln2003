"""Implementation for the ULN2003 using the MicroPython libraries"""
import utime
from uln2003 import *


class Stepper(StepperBase):
    def _set_pin(self, pin, value):
        self.pins[pin].value(value)

    def _wait(self):
        utime.sleep_ms(self.delay)
