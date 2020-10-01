from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! 13 <br> <a href='/status'>Статус</a>"

@app.route("/status")
def stataus():
    return {'status' : True, 'name': 'myMessage',  'time': datetime.datetime.today() }


app.run()