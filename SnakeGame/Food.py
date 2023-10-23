from turtle import Turtle
import random as rd


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed(0)
        self.refresh()

    def refresh(self) -> None:
        x: int = rd.randint(-280, 280)
        y: int = rd.randint(-280, 280)
        self.goto(x, y)
