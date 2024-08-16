from turtle import *

FONT = ("Futura", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto((-250, 275))
        self.ht()
        self.level = 1
        self.type()

    def type(self):
        self.write(f'Level: {self.level}', False, 'center', FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.type()

    def game_over(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Game over, your score: {self.level}", False, 'center', FONT)
