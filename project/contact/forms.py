# project/contact/forms.py

from flask_wtf import Form
from wtforms import StringField, IntegerField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Email, Length

class ContactForm(Form):
  contact_id = IntegerField()
  name = StringField('Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
  subject = SelectField('Subject', validators=[DataRequired()], choices = [('na', 'Choose One:'),
                                                                           ('Feedback', 'Feedback'),
                                                                           ('Suggestion', 'Suggestion'),
                                                                           ('Question', 'Question'),
                                                                           ('Other', 'Other')])
  message = StringField('Message', widget=TextArea())
