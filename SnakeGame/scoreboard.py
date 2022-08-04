from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("Courier", 15, "normal")
GAME_OVER_FONT = ("Courier", 35, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.hideturtle()


    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
