from turtle import *

STARTING_POSITION = (0, -270)
MOVE = 10
FINISH_LINE = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('orangered1')
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE)

    def reset(self):
        self.goto(STARTING_POSITION)

    def is_finished(self):
        if self.ycor() > FINISH_LINE:
            return True
        return False