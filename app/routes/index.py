from app import app, db
from flask import jsonify
from app.models.user import User

@app.route('/')
def index():
	return "hello ljs93444444333222!!"

@app.route('/data')
def data():
	data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
	return jsonify(data)

@app.route('/db_insert')
def db_insert():
	# person_one = User('person_1', 'hello world')
	# person_two = User('person_2', 'bye world')
	#
	# db.session.add(person_one)
	# db.session.add(person_two)
	# db.session.commit()

	output = User.query.all()
	string = ""
	for item in output:
		string = string + item.user_id + " "+ item.user_name + "<br>"
	return string
