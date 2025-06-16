# https://www.youtube.com/watch?v=e1F621aPDKw
# MAD I SQLAlchemy Part-2

from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///one_to_many.sqlite3"

db = SQLAlchemy(app)

app.app_context().push()

""" FOR ONE TO MANY RELATIONS : 
Role - parent 
User - child

one role can be given to multiple users 
but 
one user cannot have multiple roles

parent can exist independently
but 
child cannot exist independently



NOTE : Format of a foreign key (<table_name>.<attribute_name>)
"""

# Create User Model 
# child table
class User(db.Model) : 
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    password = db.Column(db.String, nullable = False) 
    role_id  = db.Column(db.Integer, db.ForeignKey('role.id'), nullable = False)
# class - User --> table - user


# Create Role Model 
# parent table
class Role(db.Model) : 
    id = db.Column(db.Integer, primary_key = True) 
    role_name = db.Column(db.String(), nullable = False, unique = True)
    users = db.relationship('User', backref = 'role')

# class - Role --> table - role
