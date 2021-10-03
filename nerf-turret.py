#!/usr/bin/env python3

import threading
import time

from Motor import Motor
from Ps4Controller import Ps4Controller

loop_int = 0.01
steps_per_loop = 1

ctrl = {

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
    stepper = Motor(
            step_pin = 18,
            direction_pin = 23,
            trans_ratio = 4)

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
    stepper = Motor(
            step_pin = 24,
            direction_pin = 25,
            trans_ratio = 3.2)

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

if __name__ == "__main__":

    az_thread = threading.Thread(
            target = az_handler,
            args = (ctrl,))
    alt_thread = threading.Thread(
            target = alt_handler,
            args = (ctrl,))
    ctrl_thread = threading.Thread(
            target = ctrl_handler,
            args = (ctrl,))

    az_thread.start()
    alt_thread.start()
    ctrl_thread.start()

    az_thread.join()
    alt_thread.join()
    ctrl_thread.join()

    print("Shutting down")
