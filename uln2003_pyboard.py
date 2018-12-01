"""Implementation for the ULN2003 using the Micropython.org pyboard"""
import pyb
from uln2003 import *


class Stepper(StepperBase):
    def _set_pin(self, pin, value):
        self.pins[pin].value(value)

    def _wait(self):
        pyb.delay(self.delay)
