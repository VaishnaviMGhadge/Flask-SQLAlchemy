from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app1 = Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db1 = SQLAlchemy(app1)

class Owner(db1.Model):
    id = db1.Column(db1.Integer, primary_key=True)
    name = db1.Column(db1.String(20))
    address = db1.Column(db1.String(100))
    pets = db1.relationship('Pet', backref='owner')

class Pet(db1.Model):
    id = db1.Column(db1.Integer, primary_key=True)
    name = db1.Column(db1.String(20))
    age = db1.Column(db1.Integer)
    owner_id = db1.Column(db1.Integer, db1.ForeignKey('owner.id'))























































"""from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app1=Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db11.sqlite3'
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 


db1=SQLAlchemy(app1)

class Owner(db1.Model):
    id=db1.Column(db1.Integer,primary_key=True)
    name=db1.Column(db1.String(30))
    address=db1.Column(db1.String(30))
    pets=db1.relationship('Pet',backref='Owner')
    


class Pet(db1.Model):
    id=db1.Column(db1.Integer,primary_key=True)
    name=db1.Column(db1.String(30))
    age=db1.Column(db1.String(30))
    owner_id=db1.Column(db1.Integer,db1.ForeignKey('owner.id'))  """
  


"""class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(100))
    pets = db.relationship('Pet', backref='owner')

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))"""


