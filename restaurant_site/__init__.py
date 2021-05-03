from flask import Flask
from flask_sqlalchemy import SQLAlchemy 




app = Flask(__name__)

app.config['SECRET_KEY'] = '8675ignl1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from restaurant_site import routes