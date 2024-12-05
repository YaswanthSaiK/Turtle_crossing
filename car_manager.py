from turtle import Turtle, Screen
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

screen = Screen()
class CarManager:
    def __init__(self):
        self.it = []
        self.yu = []
        self.position()
        self.k = 5


    def car(self, m, color):
        n = 280
        for i in range(2):
            jim = Turtle()
            jim.shape("square")
            jim.penup()
            jim.color(color)
            jim.goto(x=n, y=m)
            self.yu.append(jim)
            jim.setheading(180)
            jim.forward(5)
            n += 20


    def position(self):
        u = random.randint(0, 2)
        for i in range(u):
            colour = random.choice(COLORS)
            y = random.randint(-230, 230)
            hj = self.car(y, colour)
            self.it.append(hj)

    def movement(self):
        for i in range(2):
            for o in self.yu:
                o.forward(self.k)
        time.sleep(0.2)
        screen.update()
