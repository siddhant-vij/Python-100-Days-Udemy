from turtle import Turtle


ALIGN = "center"
FONT = ("Courier", 16, "normal")
FONT_BIG = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.writeScoreOnScreen()

    def writeScoreOnScreen(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def updateScore(self):
        self.score += 1
        self.writeScoreOnScreen()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT_BIG)
