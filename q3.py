'''
=========================================================================
Soal 3 - Cari pokemon
=========================================================================
'''

from flask import Flask, render_template, url_for, redirect,request
import json, requests

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/hasil', methods=['POST','GET'])
def hasil():
    pokemon = request.form['pokemon']
    url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon
    data = requests.get(url)
    if str(data)=='<Response [404]>':
        return redirect('error.html')

    filedata = data.json()['forms']
    
    name = filedata[0]['name']
    name1 = name.capitalize()
    picture = data.json()['sprites']
    nomor = data.json()["id"]
    height = data.json()["height"]
    weight = data.json()["weight"]

    return render_template('hasil.html', name=name1, picture=picture, nomor=nomor, height=height, weight=weight)


@app.errorhandler(404)
def page_not_found(error):
	return render_template('error.html')

if __name__ == '__main__':
	app.run(debug = True)