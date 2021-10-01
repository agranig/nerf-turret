import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
    
ms_pins = (-1, -1, -1)
direction_pin = 15
step_pin = 14

stepper1 = RpiMotorLib.A4988Nema(direction_pin, step_pin, ms_pins, "A4988")

clockwise = True
step_type = "Full"
steps = 200
step_delay = 0.0005
verbose = True
init_delay = 0.05

mymotortest.motor_go(clockwise, step_type, steps, step_delay, verbose, init_delay)

GPIO.cleanup()
