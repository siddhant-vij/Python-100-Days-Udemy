from typing import List, Tuple
from turtle import Turtle, Screen
import pandas as pd

from Scoreboard import Scoreboard


MAP_IMAGE: str = "./IndiaStateUTGuess/GuessingGame/IndiaMap.gif"
CSV_FILE: str = "./IndiaStateUTGuess/GuessingGame/IndiaStateUTsCoordinates.csv"
ALIGN: str = "center"


screen = Screen()


def getUserGuess() -> str:
    guess: str = screen.textinput(title="Guessing Game", prompt="Guess a name?")
    return guess


def initializeScreen() -> None:
    turtle: Turtle = Turtle()
    screen.setup(width=820, height=910)
    screen.title("India States & Union Territories")
    try:
        screen.addshape(MAP_IMAGE)
        turtle.shape(MAP_IMAGE)
    except:
        print("Could not load image. Make sure the path is correct.")


def initialize_data() -> List[List[str]]:
    data: pd.DataFrame = pd.read_csv(CSV_FILE)
    states: List[List[str]] = data.values.tolist()
    return states


def getStateList(stateUTs: List[Tuple[str, str, str, str]]) -> Tuple[List[str], List[str]]:
    stateList: List[str] = [state[0] for state in stateUTs if state[3] == "State"]
    utList: List[str] = [state[0] for state in stateUTs if state[3] == "UT"]
    return stateList, utList


def displayStateUTOnScreen(state: List[str]) -> None:
    pen: Turtle = Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(int(state[1]), int(state[2]))
    pen.write(state[0], align=ALIGN)


def toDoIfGuessFoundInList(guess: str, list_: List[str], stateUTsToGuess: List[List[str]]) -> None:
    for index, state in enumerate(stateUTsToGuess):
        if guess == state[0]:
            break
    displayStateUTOnScreen(stateUTsToGuess[index])
    list_.remove(guess)
    stateUTsToGuess.remove(stateUTsToGuess[index])


def allStatesGuessed(stateList: List[str], utList: List[str], score: Scoreboard) -> bool:
    if len(stateList) == 0 and len(utList) == 0:
        score.gameWon()
        return True


def gamePlay() -> None:
    initializeScreen()
    stateUTsToGuess: List[List[str]] = initialize_data()
    stateList, utList = getStateList(stateUTsToGuess)
    score: Scoreboard = Scoreboard()

    isValidState: bool = True
    while isValidState:
        guess = getUserGuess()
        if guess == "Exit":
            isValidState = False
        else:
            if guess in stateList:
                toDoIfGuessFoundInList(guess, stateList, stateUTsToGuess)
                score.updateStates()
                if allStatesGuessed(stateList, utList, score):
                    isValidState = False
            elif guess in utList:
                toDoIfGuessFoundInList(guess, utList, stateUTsToGuess)
                score.updateUTs()
                if allStatesGuessed(stateList, utList, score):
                    isValidState = False
            else:
                print(f"Incorrect Guess: {guess}")
                score.gameOver()
                isValidState = False

    screen.exitonclick()


if __name__ == "__main__":
    gamePlay()
