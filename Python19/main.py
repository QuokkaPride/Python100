from turtle import Turtle, Screen
import random

screen = Screen()
screen.listen()
colors = ("red", "green", "blue", "yellow", "pink", "orange")
screen.listen()  # Ensure the screen is listening for key presses

# Create a dictionary to store turtles with their colors
turtles = {}
starting_y = -150

game_over = False

def random_turtle_moves():
    random_color = random.choice(colors)
    turtles[random_color].forward(30)
    if turtles[random_color].pos()[0] >= 230:
        message = f"       {random_color} wins!"
        turtles[random_color].write(message, font=("arial", 20, "normal"), align = "left")
        return True
    else:
        return False

def race():
    global game_over  
    while game_over == False:
        game_over = random_turtle_moves()


for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.shapesize(stretch_wid=3, stretch_len=3)
    turtle.color(color)  
    turtles[color] = turtle
    turtles[color].penup()
    turtles[color].goto(y=starting_y, x=-230)
    starting_y += 75

screen.onkeypress(race, key="space")


screen.exitonclick()
