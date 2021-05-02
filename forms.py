from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, TextField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length




class SignupForm(FlaskForm):
    username = StringField('Enter Username', validators=[DataRequired(), Length(min=3,max=20)])
    password = StringField('Enter Password', validators=[DataRequired(), Length(min=3,max=50)])
    submit = SubmitField('Signup')


class LoginForm(FlaskForm):
    username = StringField('Enter Username', validators=[DataRequired(), Length(min=3,max=20)])
    password = StringField('Enter Password', validators=[DataRequired(), Length(min=3,max=50)])
    submit = SubmitField('Login')


class RestaurantForm(FlaskForm):
    name = StringField('Restaurant Name', validators=[DataRequired(),Length(min=3,max=20)])
    address = StringField('Address', validators=[DataRequired(), Length(min=3,max=50)])
    submit = SubmitField('Submit')


class ReviewForm(FlaskForm):
    review = TextField('Leave Review', validators=[DataRequired(), Length(min=3,max=500)])
    restaurant = QuerySelectField('Restaurant')
    submit = SubmitField('Submit Review')