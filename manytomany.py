from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,Integer,String,Column

engine=create_engine(url='sqlite3:///sample.db',echo=True)
