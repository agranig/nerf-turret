#!/usr/bin/env python3

import threading
import time

from lib.Motor import Motor
from lib.Ps4Controller import Ps4Controller
from lib.Trigger import Trigger

loop_int = 0.01
steps_per_loop = 800 # half turn in 1/8-mode

ctrl = {
    "az_stepper": None,
    "alt_stepper": None,
    "lock": threading.Lock(),
    "left": False,
    "right": False,
    "up": False,
    "down": False,
    "spin":  False,
    "fire":  False,
    "quit":  False
}

def az_handler(data):
    stepper = data["az_stepper"];

    while True:
        quit = False
        left = False
        right = False

        data["lock"].acquire()
        quit = data["quit"]
        left = data["left"]
        right = data["right"]
        data["lock"].release()

        if quit:
            break

        if left:
            print("going left")
            stepper.left(steps_per_loop)
        elif right:
            print("going right")
            stepper.right(steps_per_loop)

        time.sleep(loop_int)


def alt_handler(data):
    stepper = data["alt_stepper"];
    current_up = False
    current_down = False

    while True:
        quit = False
        up = False
        down = False

        data["lock"].acquire()
        quit = data["quit"]
        up = data["up"]
        down = data["down"]
        data["lock"].release()

        if quit:
            break

        if up:
            stepper.up(steps_per_loop)
        elif down:
            stepper.down(steps_per_loop)

        time.sleep(loop_int)

def ctrl_handler(data):
    controller = Ps4Controller(
            interface = "/dev/input/js0",
            ctrl = data)
    controller.listen()

def trigger_handler(data):
    trigger = data["trigger"];
    last_spin = False

    while True:
        fire = False

        data["lock"].acquire()
        quit = data["quit"]
        fire = data["fire"]
        spin = data["spin"]
        data["lock"].release()

        if quit:
            break

        if fire:
            trigger.trigger()

        if last_spin == False and spin == True:
            last_spin = True
            trigger.spin()
        elif last_spin == True and spin == False:
            last_spin = False
            trigger.unspin()

        time.sleep(loop_int)

if __name__ == "__main__":

    ctrl["az_stepper"] = Motor(
            step_pin = 18,
            direction_pin = 23,
            trans_ratio = 4,
            step_mode = "1/8")

    ctrl["alt_stepper"] = Motor(
            step_pin = 24,
            direction_pin = 25,
            trans_ratio = 3.2,
            step_mode = "1/16")

    ctrl["trigger"] = Trigger(
            trigger_pin = 8,
            rotor_pin = 7,
            fire_time = 0.5,
            rest_time = 0.5)

    az_thread = threading.Thread(
            target = az_handler,
            args = (ctrl,))
    alt_thread = threading.Thread(
            target = alt_handler,
            args = (ctrl,))
    ctrl_thread = threading.Thread(
            target = ctrl_handler,
            args = (ctrl,))
    trigger_thread = threading.Thread(
            target = trigger_handler,
            args = (ctrl,))

    az_thread.start()
    alt_thread.start()
    ctrl_thread.start()
    trigger_thread.start()

    az_thread.join()
    alt_thread.join()
    ctrl_thread.join()
    trigger_thread.join()

    print("Shutting down")
