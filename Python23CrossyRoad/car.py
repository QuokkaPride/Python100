from random import choice, randrange
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self = Turtle("square")
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        random_x = randrange(300, 600)
        random_y = randrange(-260, 260)
        self.goto(random_x, random_y)

    def move(self):
        self.car_speed = MOVE_INCREMENT
        self.backward(self.car_speed)  

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT  

