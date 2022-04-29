from app import app
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

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.playername.data)
        return redirect('/index')
    return render_template('search.html', title='Search', form = form)
