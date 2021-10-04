from pyPS4Controller.controller import Controller
import sys

class Ps4Controller(Controller):

    def __init__(self, **args):
        self.ctrl = args.get('ctrl')
        Controller.__init__(
                self,
                interface = args.get('interface'),
                connecting_using_ds4drv = False)

    def on_L2_press(self, value):
        print("Spinning up")
        self.ctrl["lock"].acquire()
        self.ctrl["spin"] = True
        self.ctrl["lock"].release()

    def on_L2_release(self):
        print("Spinning down")
        self.ctrl["lock"].acquire()
        self.ctrl["spin"] = False
        self.ctrl["lock"].release()

    def on_R2_press(self, value):
        print("Fire up")
        self.ctrl["lock"].acquire()
        self.ctrl["fire"] = True
        self.ctrl["lock"].release()

    def on_R2_release(self):
        print("Fire down")
        self.ctrl["lock"].acquire()
        self.ctrl["fire"] = False
        self.ctrl["lock"].release()


    def on_left_arrow_press(self):
        print("Left arrow down")
        self.ctrl["lock"].acquire()
        self.ctrl["right"] = False
        self.ctrl["left"] = True
        self.ctrl["lock"].release()

    def on_right_arrow_press(self):
        print("Left arrow down")
        self.ctrl["lock"].acquire()
        self.ctrl["left"] = False
        self.ctrl["right"] = True
        self.ctrl["lock"].release()

    def on_left_right_arrow_release(self):
        print("Left/Right arrow up")
        self.ctrl["lock"].acquire()
        self.ctrl["left"] = False
        self.ctrl["right"] = False
        self.ctrl["az_stepper"].stop()
        self.ctrl["lock"].release()

    def on_up_arrow_press(self):
        print("Up arrow down")
        self.ctrl["lock"].acquire()
        self.ctrl["down"] = False
        self.ctrl["up"] = True
        self.ctrl["lock"].release()

    def on_down_arrow_press(self):
        print("Down arrow down")
        self.ctrl["lock"].acquire()
        self.ctrl["up"] = False
        self.ctrl["down"] = True
        self.ctrl["lock"].release()

    def on_up_down_arrow_release(self):
        print("Up/Down arrow up")
        self.ctrl["lock"].acquire()
        self.ctrl["up"] = False
        self.ctrl["down"] = False
        self.ctrl["alt_stepper"].stop()
        self.ctrl["lock"].release()

    def on_options_press(self):
        print("Quit")
        self.ctrl["lock"].acquire()
        self.ctrl["quit"] = True
        self.ctrl["lock"].release()
        sys.exit()
