from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.setpos(0, y=260)
        self.pencolor("white")
        self.write(f"Score: {self.score}", True, align="center", font=("Arial", 24, "normal"))

