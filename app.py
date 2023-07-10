from flask import Flask, flash, render_template, request, redirect, session
import requests
import json

user_data = {}

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def home():
    print('home')

    if 'type' not in user_data:
        user_data['type'] = 'n'
        user_data['question'] = ''

    return render_template('home.html', type = user_data['type'], question = user_data['question'])


@app.route('/getTruth')
def getTruth():
    print('truth')

    try:
        tod_data = requests.get("https://api.truthordarebot.xyz/v1/truth?rating=pg")
        print(f'getTruth: {tod_data.status_code}')
    except:
        print('Could Not Connect')
        return '<h1>Could Not Connect</h1>'

    if tod_data.status_code == 200:
        user_data['question'] = tod_data.json()['question']
        user_data['type'] = 't'
    else:
        print('An Error Occured')
        return '<h1>An Error Occured</h1>'

    return redirect('/')

@app.route('/getDare')
def getDare():
    print('dare')

    try:
        tod_data = requests.get("https://api.truthordarebot.xyz/v1/dare?rating=pg")
        print(f'getDare: {tod_data.status_code}')
    except:
        print('Could Not Connect')
        return '<h1>Could Not Connect</h1>'

    if tod_data.status_code == 200:
        user_data['question'] = tod_data.json()['question']
        user_data['type'] = 'd'
    else:
        print('An Error Occured')
        return '<h1>An Error Occured</h1>'

    return redirect('/')

