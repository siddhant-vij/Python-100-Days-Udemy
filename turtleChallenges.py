from turtle import Turtle, Screen
import random as rd


draw = Turtle()


def drawTriangleToDecagon():
    for i in range(3, 11):
        angle = 360 / i
        draw.color(rd.random(), rd.random(), rd.random())
        for _ in range(i):
            draw.forward(100)
            draw.left(angle)


def randomWalk(numSteps):
    for _ in range(numSteps):
        draw.color(rd.random(), rd.random(), rd.random())
        draw.speed(6)
        draw.pensize(10)
        draw.forward(30)
        direction = rd.randint(1, 4)
        if direction == 1:
            draw.right(90)
        elif direction == 2:
            draw.left(90)
        elif direction == 3:
            draw.forward(90)
        else:
            draw.backward(90)


def drawSpirograph(numCircles):
    angle = 360 / numCircles
    for _ in range(numCircles):
        draw.color(rd.random(), rd.random(), rd.random())
        draw.speed(0)
        draw.circle(100)
        draw.left(angle)


# drawTriangleToDecagon()
# randomWalk(100)
drawSpirograph(100)


screen = Screen()
screen.exitonclick()
