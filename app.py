#!/usr/bin/env python

import flask
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True 

@app.route('/')
def main():
    return render_template('index.html', api_data=[])

@app.route('/fd')
def fd():
    return render_template('force-directed.html', api_data=[])

@app.route('/miserables.json')
def fd_json():
    return render_template('miserables.json', api_data=[])


if __name__ == "__main__":
    app.run(host='0.0.0.0')