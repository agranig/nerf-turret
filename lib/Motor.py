import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

class Motor:

    def __init__(self, **args):
        self.step_pin = args.get('step_pin')
        self.direction_pin = args.get('direction_pin')
        self.ms_pins = args.get('ms_pins', (-1, -1, -1))
        self.trans_ratio = args.get('trans_ratio', 1)
        self.type = args.get('type', "A4988")
        self.step_mode = args.get('step_mode', "Full")

        self.stepper = RpiMotorLib.A4988Nema(
                self.direction_pin,
                self.step_pin,
                self.ms_pins,
                self.type)

    def __turn(self, clockwise, steps):
        init_delay = 0.01
        step_delay = 0.001
        verbose = False

        self.stepper.motor_go(
                clockwise,
                self.step_mode,
                int(steps * self.trans_ratio),
                step_delay,
                verbose,
                init_delay)

    def left(self, steps):
        self.__turn(False, steps)

    def up(self, steps):
        self.__turn(False, steps)

    def right(self, steps):
        self.__turn(True, steps)

    def down(self, steps):
        self.__turn(True, steps)

    def stop(self):
        self.stepper.motor_stop()
