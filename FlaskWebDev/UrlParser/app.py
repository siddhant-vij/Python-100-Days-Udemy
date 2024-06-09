from flask import Flask
app = Flask(__name__)


@app.route("/")
def greeting():
    return "Hello, World!"


@app.route("/<string:username>/<int:age>")
def hello(username, age):
    return f"Hello {username}, you are {age} years old!"


if __name__ == "__main__":
    app.run(debug=True)
