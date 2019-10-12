"""Implementation for the ULN2003 using MicroPython for ESP8266"""
import time

from uln2003 import *


class Stepper(StepperBase):
    def _set_pin(self, pin, value):
        self.pins[pin].value(value)

    def _wait(self):
        time.sleep_ms(self.delay)
