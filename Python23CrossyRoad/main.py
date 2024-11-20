import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car import Car
from scoreboard import Scoreboard
from random import randrange

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Tippy's Highway Adventure")
screen.bgcolor("white")
screen.tracer(0)


tippy = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(tippy.move_up, "Up")
screen.onkey(tippy.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(.01)
    screen.update()

    car = Car()
    
    car.move()



    #Level Complete
    if tippy.pos() == (0, FINISH_LINE_Y):
        scoreboard.next_level()
        tippy.reset_position()



screen.exitonclick()
