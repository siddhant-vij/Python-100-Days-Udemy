import time
from turtle import Screen

from Player import Player
from Car import Car
from Scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Road Cross Game")
screen.tracer(0)

player = Player()
cars: list[Car] = []
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)
    cars.append(Car())
    for car in cars:
        car.move()
        if car.ready_for_collision and car.distance(player) < 20:
            gameIsOn = False
            scoreboard.gameOver()
        if car.isOutOfBounds():
            car.delete()
            cars.remove(car)
        if player.isAtFinishLine():
            scoreboard.updateLevel()
            player.goToStart()
            Car.increaseMoveSpeed()


screen.exitonclick()
