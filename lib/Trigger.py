import RPi.GPIO as GPIO
import time

class Trigger:

    def __init__(self, **args):
        self.trigger_pin = args.get('trigger_pin')
        self.rotor_pin = args.get('rotor_pin')
        self.fire_time = args.get('fire_time', 0.1)
        self.rest_time = args.get('rest_time', 0.1)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.output(self.trigger_pin, GPIO.LOW)

        GPIO.setup(self.rotor_pin, GPIO.OUT)
        GPIO.output(self.rotor_pin, GPIO.LOW)

    def trigger(self):
        GPIO.output(self.trigger_pin, GPIO.HIGH)
        time.sleep(self.fire_time)
        GPIO.output(self.trigger_pin, GPIO.LOW)
        time.sleep(self.rest_time)

    def spin(self):
        GPIO.output(self.rotor_pin, GPIO.HIGH)

    def unspin(self):
        GPIO.output(self.rotor_pin, GPIO.LOW)
