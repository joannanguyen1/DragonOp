from . import db
from flask_login import UserMixin

#creates a database for the user with columns for that user's significant attributes. 
#Usermixin ensures that authentication for login is executed
#inherits from the db.Model base class from SQLAlchemy 

class User(db.Model, UserMixin):
    #creates a unique id as an integer for users in a database column
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')