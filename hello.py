from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return "hello ljs93kr!!"

@app.route('/data')
def data():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)

