from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from database import db_session, init_db
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql-root@localhost/mytest?charset=utf8'
db = SQLAlchemy(app)

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
	print entries


