# hello.py
from flask import Flask, request, jsonify, make_response
from wakeonlan import send_magic_packet

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('application.cfg', silent=True)

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
    keywords = params.split(" ")
    print(type(params))
    if 'つけ' in keywords:
        send_magic_packet(app.config['MAC_ADDRESS'])
    if '消し' in keywords:
        print('ケスで')
    response = {}
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
    return make_response(jsonify(response))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
