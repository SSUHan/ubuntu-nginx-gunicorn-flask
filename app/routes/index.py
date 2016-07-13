from app import app
from flask import jsonify


@app.route('/')
def index():
	return "hello ljs93kr!!"

@app.route('/data')
def data():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)

@app.route('/show_table')
def show_table():
	queries = db_session.query(User)
	entries = [ dict(user_id=q.user_id, user_name=q.user_name, created=q.created) for q in queries]
	print(entries)