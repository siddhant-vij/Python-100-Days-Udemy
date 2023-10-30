import os
from turtle import Turtle


ALIGN = "center"
FONT = ("Courier", 16, "normal")
FONT_BIG = ("Courier", 24, "bold")
HIGH_SCORE_FILE = "./SnakeGame/HighScore.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        with open(HIGH_SCORE_FILE) as file:
            self.highScore = int(file.read() or 0)
        self.writeScoreOnScreen()

    def writeScoreOnScreen(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highScore}", align=ALIGN, font=FONT)

    def updateScore(self):
        self.score += 1
        self.writeScoreOnScreen()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT_BIG)
        if self.score > self.highScore:
            self.highScore = self.score
            with open(HIGH_SCORE_FILE, "w") as file:
                file.write(str(self.highScore))
