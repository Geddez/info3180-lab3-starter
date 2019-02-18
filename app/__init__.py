from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525' # (or try 2525)
app.config['MAIL_USERNAME'] = 'f15adbb8a95854'
app.config['MAIL_PASSWORD'] = 'ca2a4b6d3a9362'
mail = Mail(app)
from app import views