# project/main/view.py

################
#### import ####
################

from functools import wraps
from flask import flash, redirect, render_template, request, session, url_for, Blueprint

################
#### config ####
################

main_blueprint = Blueprint('main', __name__)


##########################
#### helper functions ####
##########################

def login_required(test):
  @wraps(test)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return test(*args, **kwargs)
    else:
      flash('You need to login first.')
      return redirect(url_for('main.login'))
  return wrap


################
#### router ####
################

@main_blueprint.route('/')
@main_blueprint.route('/home')
def home():
  return render_template('home.html')

@main_blueprint.route('/service')
def service():
  return render_template('service.html')

@main_blueprint.route('/access')
def access():
  return render_template('access.html')

@main_blueprint.route('/about')
def about():
  return render_template('about.html')

