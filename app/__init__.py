from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql-root@localhost/mytest?charset=utf8'
db = SQLAlchemy(app)


from app.models import *
from app.routes import *





