from app import app
<<<<<<< HEAD
from flask import render_template, flash, redirect
from app.stock import *
from app.forms import LoginForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        #print(form.playername.data)
        return redirect('/getplayerstat/'+str(form.playername.data)+"/"+str(form.year.data)+ "/" + str(form.month.data) + "/" + str(form.date.data))
    return render_template('index.html', title = "stats", form = form)
@app.route('/getplayerstat/<name>/<year>/<month>/<date>', methods=['GET','POST'])
def getplayerstat(name, year, month, date):
    d = datetime(int(year), int(month), int(date))
    test_stock = {
    "pts" : 1,
    "reb" : 1,
    "ast" : 1,
    "stl" : 1,
    "blk" : 1,
    "tov" : 1 
    }
    test_player = player_stock(test_stock, name)
    data = str(test_player.magic(d))
    return data

@app.route('/test', methods=['GET', 'POST'])
=======
from flask import render_template
from stock import *

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
>>>>>>> main
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
<<<<<<< HEAD
    test_player = player_stock(test_stock, "jamesle01")
    data = str(test_player.magic(d))
    return data

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.playername.data)
        return redirect('/index')
    return render_template('search.html', title='Search', form = form)
=======
    test_player = player_stock(test_stock, 'jamesle01', d)
    test = test_player.magic
    print(test)
    return render_template('test.html', title = "test", test_player = test_player)
>>>>>>> main
