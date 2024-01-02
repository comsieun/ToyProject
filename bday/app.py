from flask import Flask,render_template, request, abort, redirect
from http import HTTPStatus
import json

app = Flask(__name__)
memos = ['a','b','c']

@app.route("/")
def home():
    global memos
    return render_template('index.html', memos=memos)


@app.route("/memo", methods=['POST'])
def post_new_memo():
    if not request.is_json:
        print(request.data)
        abort(HTTPStatus.BAD_REQUEST)
    
    #json으로 받은 경우
    data = str(request.data)
    m = data[6:-1]
    memos.append( m )

@app.route("/memo", methods=['GET'])
def get_new_memo():
    return {'memos':memos}

if __name__ == '__main__':
    app.debug = True
    app.run()