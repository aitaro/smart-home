# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response
from wakeonlan import send_magic_packet
import winrm
import os

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

@app.route("/pc", methods=['POST'])
def postPc():
    # 苦肉の策
    if os.getenv('FLASK_ENV') == 'development':
        params = request.json
    else:
        params = request.json.encode('utf-8')
    keywords = params.split(" ")
    if 'つけ' in keywords:
        send_magic_packet(app.config['MAC_ADDRESS'])
    if '消し' in keywords:
        s = winrm.Session(app.config['DESKTOP_IP_ADDRESS'], auth=('aitaro', app.config['DESKTOP_LOGIN_PASSWORD']))
        s.run_cmd('shutdown', ['/h'])
    # if '音楽' in keywords:
    #     print('start "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --app=https://music.youtube.com')
    #     s = winrm.Session(app.config['DESKTOP_IP_ADDRESS'], auth=('aitaro', app.config['DESKTOP_LOGIN_PASSWORD']))
    #     s.run_ps(b'start "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --app=https://music.youtube.com')
    response = {}
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
    return make_response(jsonify(response))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
