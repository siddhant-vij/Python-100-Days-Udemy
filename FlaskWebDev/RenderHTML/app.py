from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1 style="color:blue; text-align:center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExczE3M2Uxd3NmYWE0cDJ6Z2oxdG51NHY2ZGxoOWh5eW9rNHFhbXFyZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/I2m1BpfpTHxUxk4C49/giphy.gif" width="500">'


@app.route("/bye")
def bye():
    return "Bye!"


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/style")
@make_bold
@make_emphasis
@make_underline
def style():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
