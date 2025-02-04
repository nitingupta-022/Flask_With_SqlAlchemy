from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.sqlite3"

db = SQLAlchemy(app)

app.app_context().push()   # <--- this will create my_database in instance folder

# Creation of table 
class User(db.Model) : 
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    password = db.Column(db.String(), nullable = False)



"""
# Creation
user_1 = User(username = "Nitin", password = "1234")
db.session.add(user_1)
db.session.commit()

# Updation
user_1 = User.query.get(1)
user_1.password = "54321"
db.session.commit()

# Deletion
user_1 = User.query.filter_by(username = "Nitin").first()
db.session.delete(user_1)
db.session.commit() 


# After commit the  changes wiil show to the database
"""