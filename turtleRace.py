from turtle import Turtle, Screen
import random as rd

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.colormode(255)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]


def getUserBet():
    isBetValid = False
    while not isBetValid:
        bet = screen.textinput(
            title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
        if bet in colors:
            isBetValid = True
            return bet


def getStartingPositions():
    positions = []
    gap = -150
    for _ in range(0, 7):
        positions.append(gap)
        gap += 50
    return positions


def drawAndPlaceTurtles(positions):
    turtles = []
    counter = 0
    for position in positions:
        turtle = Turtle(shape="turtle")
        turtle.shapesize(2, 2, 2)
        turtle.penup()
        turtle.color(colors[counter])
        counter += 1
        turtle.goto(x=-220, y=position)
        turtle.pendown()
        turtles.append(turtle)
    return turtles


def moveTurtles(turtles):
    for turtle in turtles:
        turtle.forward(rd.randint(0, 10))


def startRace():
    bet = getUserBet()
    turtles = drawAndPlaceTurtles(getStartingPositions())
    while True:
        moveTurtles(turtles)
        for turtle in turtles:
            if turtle.xcor() > 210:
                if bet == turtle.pencolor():
                    print(
                        f"You won! The {turtle.pencolor()} turtle is the winner!")
                else:
                    print(
                        f"You lost! The {turtle.pencolor()} turtle is the winner!")
                return


startRace()


screen.exitonclick()
