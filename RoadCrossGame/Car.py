from turtle import Turtle
import random as rd

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_SPEED = 10
MOVE_SPEED_INCREMENT = 10
CAR_X_BOUND = -280


class Car(Turtle):
    carSpeed = STARTING_MOVE_SPEED

    def __init__(self) -> None:
        super().__init__()
        self.ready_for_collision = False
        self.createCar()

    def createCar(self) -> None:
        if rd.random() > 0.6:
            self.penup()
            self.shape("square")
            self.color(rd.choice(COLORS))
            self.shapesize(1, 2)
            self.setheading(180)
            self.goto(300, rd.randint(-250, 250))
            self.ready_for_collision = True

    def move(self) -> None:
        self.forward(Car.carSpeed)

    @classmethod
    def increaseMoveSpeed(cls) -> None:
        cls.carSpeed += MOVE_SPEED_INCREMENT

    def isOutOfBounds(self) -> bool:
        return self.xcor() < CAR_X_BOUND

    def delete(self):
        self.hideturtle()
