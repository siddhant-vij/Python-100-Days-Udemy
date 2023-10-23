from turtle import Turtle


ALIGN = "left"
ALIGN_BIG = "center"
FONT = ("Courier", 20, "normal")
FONT_BIG = ("Courier", 40, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.level = 1
        self.goto(-290, 260)
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def updateLevel(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGN_BIG, font=FONT_BIG)
