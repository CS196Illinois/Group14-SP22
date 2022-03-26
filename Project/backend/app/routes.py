from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
@app.route('/getplayerstat/<name>', methods=['GET','POST'])
def getplayerstat(name):
    playerstat = {'s': 1}
    for key in playerstat.keys():
        print(key, playerstat[key])