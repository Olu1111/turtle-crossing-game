from turtle import *

FONT = ("Futura", 24, "normal")


class Instr(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto((0, 275))
        self.ht()
        self.level = 1
        self.type()

    def type(self):
        self.write("push 'w' to move", False, 'center', FONT)