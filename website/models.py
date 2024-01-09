#this particular python file is for database models
#here we learn how to use database models

from . import db
from flask_login import UserMixin

class Note(db.Model):
    


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))


