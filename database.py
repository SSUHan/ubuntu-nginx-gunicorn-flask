# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:mysql-root@localhost/test?charset=utf8', convert_unicode=False)

