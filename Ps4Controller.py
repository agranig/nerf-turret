from pyPS4Controller.controller import Controller
import sys

class Ps4Controller(Controller):

    def __init__(self, **args):
        self.ctrl = args.get('ctrl')
        Controller.__init__(
                self,
                interface = args.get('interface'),
                connecting_using_ds4drv = False)

    def on_L2_press(self):
        print("Spinning up")
        self.ctrl["lock"].acquire()
        self.ctrl["spin"] = True
        self.ctrl["lock"].release()

    def on_L2_release(self):
        print("Spinning down")
        self.ctrl["lock"].acquire()
        self.ctrl["spin"] = False
        self.ctrl["lock"].release()

    def on_R2_press(self):
        print("Fire up")
        self.ctrl["lock"].acquire()
        self.ctrl["fire"] = True
        self.ctrl["lock"].release()

    def on_R2_release(self):
        print("Fire down")
        self.ctrl["lock"].acquire()
        self.ctrl["fire"] = False
        self.ctrl["lock"].release()

    def on_L3_left(self, value):
        if (value > -25000):
            return
        print("Left")
        self.ctrl["lock"].acquire()
        self.ctrl["right"] = False
        self.ctrl["left"] = True
        self.ctrl["lock"].release()

    def on_L3_right(self, value):
        if (value < 25000):
            return
        print("Right")
        self.ctrl["lock"].acquire()
        self.ctrl["right"] = True
        self.ctrl["left"] = False
        self.ctrl["lock"].release()

    def on_L3_up(self, value):
        if (value > -25000):
            return
        print("Up")
        self.ctrl["lock"].acquire()
        self.ctrl["up"] = True
        self.ctrl["down"] = False
        self.ctrl["lock"].release()

    def on_L3_down(self, value):
        if (value < 25000):
            return
        print("Down")
        self.ctrl["lock"].acquire()
        self.ctrl["up"] = False
        self.ctrl["down"] = True
        self.ctrl["lock"].release()

    def on_L3_x_at_rest(self):
        print("No Left/Right")
        self.ctrl["lock"].acquire()
        self.ctrl["left"] = False
        self.ctrl["right"] = False
        self.ctrl["lock"].release()

    def on_L3_y_at_rest(self):
        print("No Up/Down")
        self.ctrl["lock"].acquire()
        self.ctrl["up"] = False
        self.ctrl["down"] = False
        self.ctrl["lock"].release()

    def on_options_press(self):
        print("Quit")
        self.ctrl["lock"].acquire()
        self.ctrl["quit"] = True
        self.ctrl["lock"].release()
        sys.exit()
