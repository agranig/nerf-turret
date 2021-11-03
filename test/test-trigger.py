#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

port = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.OUT)
GPIO.output(port, GPIO.LOW)

for i in range(50):
    GPIO.output(port, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(port, GPIO.LOW)
    time.sleep(0.05)
