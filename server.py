from flask import Flask, Response, request
import time
from datetime import datetime

app = Flask(__name__)
db = [
            {'text': 'Привет', 'author': 'Jack', 'time': time.time()},
            {'text': 'Привет!', 'author': 'Mary', 'time': time.time()},
        ]

@app.route("/")
def hello():
    return "Hello, World! 13 <br> <a href='/status'>Статус</a>"

@app.route("/status")
def stataus():
    time_now = datetime.now()
    return {'status' : True,
            'name': 'myMessager',
            'time': time_now
    }
@app.route("/send_message", methods =['POST'])
def send_message():
    data = request.json
    if not isinstance(data, dict):
        return Response('not json', 400)

    text = data.get('text')
    author = data.get('author')

    if isinstance(text, str) and isinstance(author, str):
        db.append({
                'text': text,
                'author': author,
                'time': datetime.now()
        })
        return Response('ok')
    else:
        return Response('wrong', 400)

@app.route("/get_message")
def get_messages():
    after = request.args.get('after',0)
    try:
        after = float(after)
    except:
        return Response ('wrong', 400)

    new_message = [m for m in db if m['time'] > after]
    return {'messages' : new_message}


app.run()