"""Number Guessing Game

This script simulates a number guessing game using your web browser.

This script requires that 'flask' be installed within the Python
environment you are running this script in.

"""

from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(1,10)
color_list = ['301b3f', '3c415c', 'b4a5a5', '387c6d', '4e3620', '810000', 'e48257', 'd49d42', 'e4bad4', '007580']

@app.route('/')
def hello_world():
    """called when the user makes a GET request to the index URL

    :returns: the HTML rendered by the browser
    """
    return '<h1>Guess a number between 0 and 9!</h1>' \
           '<img src="https://media1.giphy.com/media/b3rveIiz8xcdi/giphy.gif?cid=ecf05e478gx8z9y4kdtqiik1c769qj6omplow7t37816zch0&rid=giphy.gif"' \
           ' alt="random number gif">'

@app.route('/<int:number>')
def number_game(number):
    """called when the user makes a GET request to /<int> URL

    :param number: a guess about the secret integer
    :return: the HTML rendered by the browser, depending on if the user guessed the secret integer correctly
    """
    if number == random_number:
        return f'<h1 style="color: {random.choice(color_list)}">You found me!</h1>' \
               f'<img src="https://media2.giphy.com/media/jmRvJC6azvbV1vBUVG/giphy.gif?cid=ecf05e478gx8z9y4kdtqiik1c769qj6omplow7t37816zch0&rid=giphy.gif" ' \
               f'alt="You found me!">'
    elif number > random_number:
        return f'<h1 style="color:{random.choice(color_list)}">Too high! Try again!</h1>' \
               f'<img src="https://media4.giphy.com/media/jTrMNc8FPZntcZmSS7/giphy.gif?cid=ecf05e470wispwo1wpn7w7pq6hdqplao7kbavclfqiec5b56&rid=giphy.gif"' \
               f'alt="Too high!">'
    else:
        return f'<h1 style="color:{random.choice(color_list)}">Too low! Try Again!</h1>' \
               f'<img src="https://media3.giphy.com/media/iF0ZpMdG4bCX9Nrwmi/giphy.gif?cid=ecf05e470wispwo1wpn7w7pq6hdqplao7kbavclfqiec5b56&rid=giphy.gif"' \
               f'alt="Too low!">'


if __name__ == '__main__':
    app.run()