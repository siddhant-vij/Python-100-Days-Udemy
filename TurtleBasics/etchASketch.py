from turtle import Turtle, Screen

draw = Turtle()
screen = Screen()


def moveForward():
    draw.forward(10)


def moveBackward():
    draw.backward(10)


def turnLeft():
    draw.left(10)


def turnRight():
    draw.right(10)


def clearScreen():
    draw.clear()
    draw.penup()
    draw.home()
    draw.pendown()


def etchAsketch():
    screen.listen()
    screen.onkey(key="w", fun=moveForward)
    screen.onkey(key="s", fun=moveBackward)
    screen.onkey(key="a", fun=turnLeft)
    screen.onkey(key="d", fun=turnRight)
    screen.onkey(key="c", fun=clearScreen)


etchAsketch()

screen.exitonclick()
