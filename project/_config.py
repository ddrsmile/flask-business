import os, random, string

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

# create random key
def create_random_key(size=10, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

# basic setting
DATABASE = 'business.db'
WTF_CSRF_ENABLED = True
SECRET_KEY = create_random_key()
DEBUG = True

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

# EMAIL setting
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'dev.nansa@gmail.com'
MAIL_PASSWORD = 'p@$$W0rd'
