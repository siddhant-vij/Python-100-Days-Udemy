import math
import random as rd
from flask import Flask

app = Flask(__name__)

randomNumber = math.floor(rd.random() * 10)
print(randomNumber)


@app.route("/")
def index():
    return '<h1 style="text-align:center">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=500 style="display:block;margin:auto"/>'


@app.route("/<int:number>")
def guess(number):
    if number > randomNumber:
        return '<h1 style="text-align:center">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=500 style="display:block;margin:auto"/>'
    elif number < randomNumber:
        return '<h1 style="text-align:center">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=500 style="display:block;margin:auto"/>'
    else:
        return '<h1 style="text-align:center">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=500 style="display:block;margin:auto"/>'


if __name__ == "__main__":
    app.run(debug=True)
