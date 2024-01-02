from flask import Flask,render_template, request, abort
from http import HTTPStatus

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
    json_data = request.json
    m = json_data.get('msg')
    memos.append(m)
    return render_template('index.html', memos=memos), HTTPStatus.OK

if __name__ == '__main__':
    app.debug = True
    app.run()