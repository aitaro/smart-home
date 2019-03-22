# hello.py
from flask import Flask, request, jsonify, make_response
from wakeonlan import send_magic_packet
app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola World!"

@app.route("/hoge", methods=['GET'])
def getHoge():
    # URLパラメータ
    params = request.args
    response = {}
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
    return make_response(jsonify(response))

@app.route("/hoge", methods=['POST'])
def postHoge():
    # ボディ(application/json)パラメータ
    params = request.json
    print(params)
    response = {}
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
    return make_response(jsonify(response))

app.run(host="127.0.0.1", port=5000)
