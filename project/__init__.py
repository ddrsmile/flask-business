# project/__init__.py

import datetime
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.mail import Message, Mail
from flask.ext.googlemaps import GoogleMaps

app = Flask(__name__)
app.config.from_pyfile('_config.py')
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
mail = Mail(app)
GoogleMaps(app)

# setting basic info of message to be sent
msg = Message(sender='dev.nansa@gmail.com', recipients=['nansaryu@gmail.com'])

# register blueprint
from project.main.views import main_blueprint
from project.contact.views import contact_blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(contact_blueprint)

@app.errorhandler(404)
def page_not_found(error):
  if app.debug is not True:
    now = datetime.datetime.now()
    r = request.url
    with open('error.log', 'a') as f:
      current_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
      f.write("\n404 error at {}:{}".format(current_timestamp, r))
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
  db.session.rollback()
  if app.debug is not True:
    now = datetime.datetime.now()
    r = request.url
    with open('error.log', 'a') as f:
      current_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
      f.write("\n500 error at {}:{}".format(current_timestamp, r))
  return render_template('500.html'), 500
