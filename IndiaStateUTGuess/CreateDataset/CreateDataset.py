import csv
from turtle import Turtle, Screen


IMAGE_FILE = "./IndiaStateUTGuess/CreateDataset/IndiaMap.gif"
OUTPUT_CSV_FILE = "./IndiaStateUTGuess/CreateDataset/IndiaStatesCoordinates.csv"


turtle = Turtle()
screen = Screen()
screen.title("India States Game")

try:
    screen.addshape(IMAGE_FILE)
    turtle.shape(IMAGE_FILE)
except:
    print("Could not load image. Make sure the path is correct.")


data = []


try:
    with open(OUTPUT_CSV_FILE, "x", newline='') as outputFile:
        dictWriter = csv.DictWriter(outputFile, fieldnames=["state", "x", "y"])
        dictWriter.writeheader()
except FileExistsError:
    pass


def getMouseClickCoordinate(x, y):
    stateName = screen.textinput("State Name", "Name of this state?")
    if stateName:
        coordinates = {"state": stateName, "x": x, "y": y}
        print(f"Captured: {coordinates}")

    keys = ["state", "x", "y"]
    with open(OUTPUT_CSV_FILE, "a", newline='') as outputFile:
        dictWriter = csv.DictWriter(outputFile, fieldnames=keys)
        dictWriter.writerow(coordinates)


screen.onclick(getMouseClickCoordinate)
screen.mainloop()
