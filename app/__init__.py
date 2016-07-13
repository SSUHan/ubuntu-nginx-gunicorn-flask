from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/mytest?charset=utf8'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


from app.models import *
from app.routes import *

db.create_all()


