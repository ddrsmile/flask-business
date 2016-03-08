# project/models.py

from project import db
import datetime

class Contact(db.Model):
  __tablename__ = "contacts"

  contact_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=False)
  subject = db.Column(db.String, nullable=False)
  message = db.Column(db.String, nullable=False)
  response = db.Column(db.String)
  user_id = db.Column(db.Integer)
  status = db.Column(db.Integer, default = 0)
  open_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
  read_date = db.Column(db.DateTime)
  closed_date = db.Column(db.DateTime)

  def __init__(self, name, email, subject, message):
    self.name = name
    self.email = email
    self.subject = subject
    self.message = message

  def __repr__(self):
    return '<name {0}>'.format(self.name)

class User(db.Model):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  password = db.Column(db.String, nullable=False)
  role = db.Column(db.String, nullable=False)

  def __init__(self, name, email, password, role):
    self.name = name
    self.email = email
    self.passwrod = password
    self.role = role

  def __repr__(self):
    return '<User {0}>'.format(self.name)
