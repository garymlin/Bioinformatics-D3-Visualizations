#!/usr/bin/env python

import flask
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True 

@app.route('/')
def main():

    return render_template('index.html', api_data=[])


if __name__ == "__main__":
    app.run(host='0.0.0.0')