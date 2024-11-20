from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1 
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-260,260)
        self.write_level()

    def next_level(self):
        self.level += 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}",  align="left", font=(FONT))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER, TIPPY",  align="center", font=("Arial", 45, "normal"))

