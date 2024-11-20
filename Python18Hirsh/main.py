import colorgram
from turtle import Turtle, Screen
from random import randrange


screen = Screen()
screen.colormode(255)

diana = Turtle()
diana.shape("turtle")

# Extract 8 colors from an image.
colors = colorgram.extract(
    "c:/Users/quokka/Documents/Engineering Fun/Python100/Python18Hirsh/image.jpg",
    NUM_COLORS,
)

NUM_COLORS = 10
SPACING = 20
DOTS_IN_ROW = 10
WIDTH = 10
ROWS = 5


def draw_dot():
    for _ in range(DOTS_IN_ROW):
        diana.pencolor(colors[randint(NUM_COLORS - 1)].rgb)
        diana.down()
        diana.forward(1)
        diana.up()
        diana.forward(SPACING)


def draw_row():
    for _ in range(ROWS):
        draw_dot()
        diana.right(90)
        diana.forward(SPACING + 1)
        diana.right(90)
        draw_dot()
        diana.left(90)
        diana.forward(SPACING)
        diana.pencolor(colors[randrange(0, NUM_COLORS - 1)].rgb)
        diana.down()
        diana.forward(1)
        diana.up()
        diana.left(90)


def make_art():
    diana.hideturtle()
    diana.speed(0)
    diana.width(WIDTH)
    draw_row()


make_art()


screen.exitonclick()
