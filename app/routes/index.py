from app import app
from flask import jsonify


@app.route('/')
def index():
	return "hello ljs93444444333222!!"

@app.route('/data')
def data():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)



