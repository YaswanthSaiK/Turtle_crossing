from turtle import Turtle
from player import Player
from car_manager import CarManager
FONT = ("Courier", 24, "normal")

care = CarManager()
playe = Player()
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.h = 0
        self.penup()
        self.hideturtle()
        # self.goto(0, 280)
        # self.write(f"Level - {self.h}", True , align="center", font=("ariel", 14, "normal"))

    def levelup(self):
        self.h += 1
        self.clear()
        self.goto(0, 280)
        self.write(f"Level - {self.h}", True, align="center", font=("ariel", 14, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAMEOVER", True, align="center", font=("ariel", 14, "normal"))
