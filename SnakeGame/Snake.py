from turtle import Turtle
from typing import List


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments: List[Turtle] = []
        self.createStartingSnake()
        self.head: Turtle = self.segments[0]

    def createStartingSnake(self) -> None:
        for position in range(3):
            self.addSegment(position)

    def addSegment(self, position: int) -> None:
        newSegment: Turtle = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position * -20, 0)
        self.segments.append(newSegment)

    def move(self) -> None:
        for segNum in range(len(self.segments) - 1, 0, -1):
            new_x: int = self.segments[segNum - 1].xcor()
            new_y: int = self.segments[segNum - 1].ycor()
            self.segments[segNum].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
