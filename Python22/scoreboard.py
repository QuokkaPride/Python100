from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position,260)
        self.write(f"Score: {self.score}",  align="center", font=("Arial", 24, "normal"))

    def score_point(self):
        self.score += 1 
        self.clear()
        self.write(f"Score: {self.score}",  align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER, SALLY",  align="center", font=("Arial", 45, "normal"))
