import colorgram
from turtle import Turtle, Screen
import random as rd


draw = Turtle()
screen = Screen()
screen.colormode(255)


def extractColors(filename):
    colors = colorgram.extract(filename, 30)
    rgb_colors = []
    for color in colors:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return rgb_colors


def moveStartingPoint():
    draw.penup()
    draw.goto(-250, -250)
    draw.pendown()


def drawHirstSpotPainting(width, height):
    draw.hideturtle()
    colorChoice = extractColors("ref-image.png")
    moveStartingPoint()
    draw.speed(0)
    for _ in range(height):
        position = draw.pos()
        for _ in range(width):
            draw.pendown()
            draw.dot(20, rd.choice(colorChoice))
            draw.penup()
            draw.forward(50)
        draw.goto(position)
        draw.left(90)
        draw.forward(50)
        draw.right(90)


drawHirstSpotPainting(10, 10)


screen.exitonclick()
