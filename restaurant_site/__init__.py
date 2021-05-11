from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from dotenv import load_dotenv
import os
from flask_login import LoginManager

load_dotenv()




app = Flask(__name__)

app.config['SECRET_KEY'] = '8675ignl1'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from restaurant_site import routes

with app.app_context():
    db.create_all()