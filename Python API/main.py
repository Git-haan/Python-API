from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World!'

@app.route('/hello', methods=['POST'])
def hello_post():
    data = request.get_json()
    return jsonify(data)

@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    return f'Hello, {name}!'

@app.route('/hello/<name>', methods=['POST'])
def hello_name_post(name):
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
