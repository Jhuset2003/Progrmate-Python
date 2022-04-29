from turtle import Turtle

FONT = ("Arial",24,"bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0 #atributo
        self.goto(0 , 260)
        self.color("Red")
        self.update_score()
        self.penup()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score {self.score}", align="center",font= FONT)

    def increased_score(self):
        self.clear()
        self.score += 1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over! :(", align="center",font= FONT)


