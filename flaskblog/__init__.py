import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail  



app=Flask(__name__)
app.config['SECRET_KEY']='e46165afab2a0992081b372a1eaee11b'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///C:\\code-files\\flask-tutorial\\flaskblog\\site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'  # type: ignore
login_manager.login_message_category='info'
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']=os.environ.get('EMAIL_PASS')
mail=Mail(app)


from flaskblog import routes