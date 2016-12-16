#!/usr/bin/env python

import flask
from flask import Flask, render_template, redirect

app = Flask(__name__)
app.debug = True 

@app.route('/')
def main():
    return redirect('/fd')

# FORCE DIRECTED GRAPH
@app.route('/fd')
def fd():
    return render_template('force-directed.html', api_data=[])

@app.route('/fd-every-10')
def fd_every_10():
    return render_template('force-directed-every-10.html', api_data=[])

@app.route('/fd-1500')
def fd_1500():
    return render_template('force-directed-1500.html', api_data=[])

@app.route('/fd-5000')
def fd_5000():
    return render_template('force-directed-5000.html', api_data=[])

@app.route('/fd-10000')
def fd_10000():
    return render_template('force-directed-10000.html', api_data=[])

# COLORED MATRIX 
@app.route('/matrix')
def matrix():
    return render_template('matrix.html', api_data=[])

@app.route('/d3-adjacency-matrix-layout.js')
def d3_adjacency_matrix_layout():
    return render_template('d3-adjacency-matrix-layout.js', api_data=[])

# TEST - MISERABLES
@app.route('/miserables.json')
def miserables():
    return render_template('miserables.json', api_data=[])

@app.route('/miserables_2.json')
def miserables_2():
    return render_template('miserables_2.json', api_data=[])

# JSON DATA OFFSIDES
@app.route('/drugs_effects.json')
def fd_json():
    return render_template('drugs_effects.json', api_data=[])

@app.route('/drugs_effects_200.json')
def fd_json_200():
    return render_template('drugs_effects_200.json', api_data=[])

@app.route('/drugs_effects_every_10.json')
def fd_json_every_10():
    return render_template('drugs_effects_every_10.json', api_data=[])

@app.route('/drugs_effects_every_50.json')
def fd_json_every_50():
    return render_template('drugs_effects_every_50.json', api_data=[])

@app.route('/drugs_effects_offsides_first1500.json')
def fd_json_offsides_first_1500():
    return render_template('drugs_effects_offsides_first1500.json', api_data=[])

@app.route('/drugs_effects_offsides_first10000.json')
def fd_json_offsides_first_10000():
    return render_template('drugs_effects_offsides_first10000.json', api_data=[])

# FINAL DATA 
@app.route('/final-2000.json')
def fd_json_offsides_final_2000():
    return render_template('final-2000.json', api_data=[])

@app.route('/final-1500.json')
def fd_json_offsides_final_1500():
    return render_template('final-1500.json', api_data=[])

@app.route('/final-5000.json')
def fd_json_offsides_final_5000():
    return render_template('final-5000.json', api_data=[])

@app.route('/final-10000.json')
def fd_json_offsides_final_10000():
    return render_template('final-10000.json', api_data=[])

@app.route('/final-50000.json')
def fd_json_offsides_final_50000():
    return render_template('final-50000.json', api_data=[])

# JSON DATA TWOSIDES
@app.route('/drugs_effects_twosides_first1500.json')
def matrix_json_twosides_first_1500():
    return render_template('drugs_effects_twosides_first1500.json', api_data=[])

@app.route('/drugs_effects_twosides_first50000.json')
def matrix_json_twosides_first_50000():
    return render_template('drugs_effects_twosides_first50000.json', api_data=[])

# ABOUT
@app.route('/about')
def about():
    return render_template('about.html', api_data=[])

if __name__ == "__main__":
    app.run(host='0.0.0.0')