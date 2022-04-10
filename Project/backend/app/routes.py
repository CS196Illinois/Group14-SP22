from app import app
from flask import render_template
import stock.py

@app.route('/')
@app.route('/index')
def index():
    stats = {"scurry": 1, "dgreen": 2, "kdurant": 3}
    return render_template('index.html', title = "stats", stats = stats)
@app.route('/getplayerstat/<name>', methods=['GET','POST'])
def getplayerstat(name):
    playerstat = {'s': 1}
    for key in playerstat.keys():
        print(key, playerstat[key])
