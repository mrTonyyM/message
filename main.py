from flask import Flask
app = Flask(__name__)

@app.rout()
def hello():
    return('Hello word')


app.run