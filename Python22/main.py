from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Beer Pong")
screen.bgcolor("black")
screen.tracer(0)


l_paddle = Paddle("Left")
r_paddle = Paddle("Right")
ball = Ball()
l_scroreboard = Scoreboard(-200)
r_scroreboard = Scoreboard(200)

screen.listen()

#move Paddles control
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()  

    #detect collision wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()


    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    #detecet miss on right
    if ball.xcor()>360:
        l_scroreboard.score_point()
        ball.reverse_position()

    #detecet miss
    if ball.xcor()<-360:
        r_scroreboard.score_point()
        ball.reverse_position()

        




screen.exitonclick()
