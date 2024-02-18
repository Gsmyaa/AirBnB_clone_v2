#!/usr/bin/python3
""" script that starts a Flask web application
    listening on 0.0.0.0, port 5000
    use the option strict_slashes=False in route definition """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ hello_hbnb method """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def only_hbnb():
    """ only_hbnb method """
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def only_c(text):
    """ only_c method: route to return C followed by text variable, replaces _
        with spaces """
    text = text.replace('_', ' ')
    return ('C' + ' ' + text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
