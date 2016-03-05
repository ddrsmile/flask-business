# project/contact/view.py

################
#### import ####
################

from functools import wraps
from flask import render_template, request, session, Blueprint
from sqlalchemy.exc import IntegrityError
from .forms import ContactForm
from project import app, db, mail, msg
from project.models import Contact
from threading import Thread


################
#### config ####
################

contact_blueprint = Blueprint('contact', __name__)


##########################
#### helper functions ####
##########################

def async(test):
  @wraps(test)
  def wrap(*args, **kwargs):
    thr = Thread(target = test, args = args, kwargs = kwargs)
    thr.start()
  return wrap

@async
def send_async_email(app, msg):
  with app.app_context():
    mail.send(msg)

def send_email(name, email, subject, message):
  msg.subject = subject
  msg.body = """
  From: %s <%s>
  %s
  """ % (name, email, message)
  send_async_email(app, msg)



################
#### router ####
################

@contact_blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
  error=None
  form = ContactForm(request.form)
  print(request.method)
  if request.method == 'POST':
    if form.validate_on_submit():
      new_contact = Contact(form.name.data,
                            form.company.data,
                            form.email.data,
                            form.subject.data,
                            form.message.data)
      send_email(form.name.data, form.email.data, form.subject.data, form.message.data)
      try:
        db.session.add(new_contact)
        db.session.commit()
        return render_template('contact.html', success=True)
      except IntegrityError:
        error = 'Please check the information you input'
        return render_template('contact.html', form=form, error=error)
  return render_template('contact.html', form=form, error=error)
