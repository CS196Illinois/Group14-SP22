<<<<<<< HEAD

from flask import Flask
#from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
#app.config.from_object(Config)
=======
from flask import Flask

app = Flask(__name__)
>>>>>>> main

from app import routes