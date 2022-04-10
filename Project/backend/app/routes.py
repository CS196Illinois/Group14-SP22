from app import app
from flask import render_template
from app.stock import *

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

@app.route('/test')
def test():
    d = datetime(2018, 6, 8)
    test_stock = {
    "pts" : 1,
    "reb" : 1,
    "ast" : 1,
    "stl" : 1,
    "blk" : 1,
    "tov" : 1 
    }
    test_player = player_stock(test_stock, "jamesle01")
    data = str(test_player.magic(d))
    return data
