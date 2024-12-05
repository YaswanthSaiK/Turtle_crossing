import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
play = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(play.moves, "Up")
score.levelup()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.position()
    if car.k == 5:
        for i in range(4):
            car.movement()
    else:
        car.movement()
    if play.ycor() >= 280:
        play.goto(0, -280)
        car.k += 10
        score.levelup()
    for k in car.it:
        for i in range(2):
            for o in car.yu:
                if play.distance(o) < 20:
                    score.gameover()
                    game_is_on = False



screen.exitonclick()
