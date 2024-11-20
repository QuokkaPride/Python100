from turtle import Turtle, Screen
import random


screen = Screen()
screen.colormode(255)  

princess_diana = Turtle()
princess_diana.shape("turtle")
princess_diana.color("lightpink3")

def generate_random_rgb():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    return (red, green, blue)

def circle(circles):
    for _ in range (360):
        princess_diana.forward(1)
        princess_diana.right(1)
    for _ in circles:
        princess_diana.right(1)


circle(500)


# def random_walk(turns):
#     for _ in range(turns):
#         princess_diana.pensize(7)
#         princess_diana.speed(0)
#         princess_diana.forward(15)
#         princess_diana.right(random.choice([0,90,120,180,270]))
#         random_rgb = generate_random_rgb()
#         princess_diana.color(random_rgb)

# random_walk(300)













# def draw_shape(sides):
#     turn_angle = 360 / sides
#     for _ in range(sides):
#         princess_diana.forward(100)
#         princess_diana.right(turn_angle)

# for sides in range(11):
#     if sides > 2:     
#         draw_shape(sides)
#     random_rgb = generate_random_rgb()
#     princess_diana.color(random_rgb)

screen.exitonclick()
