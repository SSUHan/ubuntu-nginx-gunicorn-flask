from app import app, db
from flask import jsonify, request
from app.models.user import User

@app.route('/')
def index():
	return "hello ljs93kr!!"

@app.route('/data')
def data():
	data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
	return jsonify(data)

@app.route('/db_insert', methods=['GET'])
def db_insert():
	user_id = request.args.get('user_id')
	user_name = request.args.get('user_name')

	person = User(user_id, user_name)

	db.session.add(person)
	db.session.commit()

	output = User.query.all()
	string = ""
	for item in output:
		string = string + item.user_id + " "+ item.user_name + "<br>"
	return string
