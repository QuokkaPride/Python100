from turtle import Turtle
from turtle import Screen
screen = Screen()

player_name = screen.textinput("Player Name", "Enter your name:")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}",  align="center", font=("Comic Sans MS", 24, "normal"))

    def score_point(self):
        self.score += 1 
        self.clear()
        self.write(f"Score: {self.score}",  align="center", font=("Comic Sans MS", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER\n {player_name}",  align="center", font=("Comic Sans MS", 45, "normal"))
