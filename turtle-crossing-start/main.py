import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from instr import Instr

screen = Screen()
screen.bgcolor('aquamarine1')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
car = CarManager()
do = Instr()
screen.onkey(player.move, 'w')

game = True
while game:
    time.sleep(0.1)
    screen.update()
    car.new_car()
    car.rush()

    if player.ycor() > -250:
        do.clear()

    if player.is_finished():
        player.reset()
        car.speed_up()
        score.update()

    for vehicle in car.traffic:
        if vehicle.distance(player) < 25:
            game = False
            score.game_over()
            player.ht()


screen.exitonclick()
