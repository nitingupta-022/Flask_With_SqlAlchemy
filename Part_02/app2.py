from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///many_to_many.sqlite3"

db = SQLAlchemy(app) 

app.app_context().push()

"""
FOR MANY TO MANY RELATIONS : 

they can co-exist and independent

one role can be given to many users
and 
one user can have many roles


"""


# Create User Model : 
class User(db.Model) : 
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    password = db.Column(db.String(), nullable = False)
    roles = db.relationship('Role', backref = "users", secondary = 'association')

# Create Role Model : 
class Role(db.Model) : 
    id = db.Column(db.Integer, primary_key = True)
    role_name = db.Column(db.String(20), nullable = False, unique = True)

# Create Association Model
class Association(db.Model) : 
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))


"""
***** TERMINAL PART ******

>>> from app2 import *
>>> db.create_all()
>>> user_1 = User.query.filter_by(username = "user_1").first()
>>> user_1.id
1
>>> user_1.password
'12345'
>>> user_1.username
'user_1'
>>> user_1.roles
[]
>>> role_1 = Role.query.filter_by(role_name = 'Student').first()
>>> role_1.users
[]
>>> role_1.users.append(user_1)
>>> role_1.users
[<User 1>]
>>> user_1.roles
[<Role 3>]
>>> db.session.commit()
>>> user_2 = User.query.filter_by(username = "user_2").first
>>> user_2.username
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute 'username'
>>> user_2 = User.query.filter_by(username = "user_2").first()
>>> user_2.username
'user_2'
>>> role_2 = Role.query.get(1)                   
<stdin>:1: LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
>>> role_2.role_name
'Admin'
>>> role_2.users.append(user_2) 
>>> role_2.users
[<User 2>]
>>> db.session.commit()
>>> user_2.roles
[<Role 1>]
>>> role_2.users
[<User 2>]
>>> user_1.roles.append(role_2)
>>> db.session.commit()
>>> user_1.roles
[<Role 3>, <Role 1>]
>>> user_2.roles.append(role_1)
>>> db.session.commit()
>>> user_2.roles
[<Role 1>, <Role 3>]
>>> role_2.users
[<User 2>, <User 1>]
>>> role_3 = Role.query.get(2)
>>> user_1.roles.append(role_3)
>>> user_1.roles
[<Role 3>, <Role 1>, <Role 2>]
>>> db.session.commit()
"""