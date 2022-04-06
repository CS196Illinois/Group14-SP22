from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    desserts = {"taylor": "ice cream", "sarah": "tiramisu", "jeff": "cherry pie"}
    return render_template('index.html', title="home", desserts=desserts)