#!/usr/bin/env python3

import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

az_ms_pins = (-1, -1, -1)
az_step_pin = 18
az_direction_pin = 23

alt_ms_pins = (-1, -1, -1)
alt_step_pin = 24
alt_direction_pin = 25

az_factor = 4
alt_factor = 3.2

az_stepper = RpiMotorLib.A4988Nema(az_direction_pin, az_step_pin, az_ms_pins, "A4988")
alt_stepper = RpiMotorLib.A4988Nema(alt_direction_pin, alt_step_pin, alt_ms_pins, "A4988")

clockwise = False
step_type = "Full"
steps = int(200 * az_factor)
step_delay = 0.001
verbose = True
init_delay = 0.01

az_stepper.motor_go(clockwise, step_type, steps, step_delay, verbose, init_delay)

clockwise = False
step_type = "Full"
steps = int(200 * alt_factor)
step_delay = 0.001
verbose = True
init_delay = 0.05
alt_stepper.motor_go(clockwise, step_type, steps, step_delay, verbose, init_delay)
