# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response
from wakeonlan import send_magic_packet

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('application.cfg', silent=True)

@app.route("/")
def route():
    return "Hello! this is the aitaro's server"

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
    # print(request)
    # print('hogeghoggeg')
    # print(request.json)
    params = request.json
    # print(params.decode('utf-8'))
    keywords = params.split(" ")
    # print(keywords)
    # print(type(params))
    if 'つけ' in keywords:
        send_magic_packet(app.config['MAC_ADDRESS'])
    if '消し' in keywords:
        print('shut down')
    response = {}
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
    return make_response(jsonify(response))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
