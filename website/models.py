from . import db
from flask_login import UserMixin
from sqlalchemy.orm import func

class User(db.Model, UserMixin):
  # __tablename__='users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(50))
  first_name = db.Column(db.String)
  notes = db.relationship('Note')
  # notes = db.relationship('Note', backref='user')

class Note(db.Model):
  # __tablename__ ='notes'
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String)
  date_created = db.Column(db.DateTime(timezone=True), default=func.now())
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

