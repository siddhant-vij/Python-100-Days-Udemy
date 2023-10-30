from turtle import Turtle
from typing import Tuple


ALIGN: str = "center"
FONT: Tuple[str, int, str] = ("Courier", 20, "normal")
FONT_BIG: Tuple[str, int, str] = ("Courier", 40, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.states: int = 0
        self.uts: int = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(270, 270)
        self.writeScoreOnScreen()

    def writeScoreOnScreen(self) -> None:
        self.clear()
        self.write(f"States: {self.states}\nUTs: {self.uts}", align=ALIGN, font=FONT)

    def updateStates(self) -> None:
        self.states += 1
        self.writeScoreOnScreen()

    def updateUTs(self) -> None:
        self.uts += 1
        self.writeScoreOnScreen()

    def gameOver(self) -> None:
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT_BIG)

    def gameWon(self) -> None:
        self.goto(0, 0)
        self.write("You've Won!", align=ALIGN, font=FONT_BIG)
