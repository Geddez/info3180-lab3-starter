from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextField
from wtforms.validators import DataRequired 

class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    subject = StringField('subject', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    text = TextField('text',validators=[DataRequired()])