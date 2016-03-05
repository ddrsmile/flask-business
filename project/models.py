# project/models.py

from project import db

class Contact(db.Model):
  __tablename__ = "contacts"

  contact_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  company = db.Column(db.String)
  email = db.Column(db.String, nullable=False)
  subject = db.Column(db.String)
  message = db.Column(db.String)

  def __init__(self, name, company, email, subject, message):
    self.name = name
    self.company = company
    self.email = email
    self.subject = subject
    self.message = message

  def __repr__(self):
    return '<name {0}>'.format(self.name)
