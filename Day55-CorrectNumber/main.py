from flask import Flask
import random

random_num = random.randint(0, 9)

app = Flask(__name__)

@app.route("/")
def display():
    return "<h1> Guess a number between 0 and 9 </h1>" \
        "<img src='https://media4.giphy.com/media/eikX1hbwlRkAQR8LAk/200w.webp?cid=ecf05e475fwtr89twvca9ml2lamrywknhp5gf8s7r4v456z8&rid=200w.webp&ct=g'/>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_num:
        return "<h1> Too high </h1>"
    elif guess < random_num:
        return "<h1> Too low </h1>"
    else:
        return "<h1 style= 'color: green'>You found me!</h1>"

if __name__ == "__main__":
    app.run(debug=True)