from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length



class SignupForm(FlaskForm):
    username = StringField('Enter Username', validators=[DataRequired(), Length(min=3,max=50)])
    password = StringField('Enter Password', validators=[DataRequired(), Length(min=3,max=50)])
    submit = SubmitField('Signup')


class LoginForm(FlaskForm):
    username = StringField('Enter Username', validators=[DataRequired(), Length(min=3,max=50)])
    password = StringField('Enter Password', validators=[DataRequired(), Length(min=3,max=50)])
    submit = SubmitField('Login')


class RestaurantForm(FlaskForm):
    name = StringField('Restaurant Name', validators=[DataRequired(),Length(min=3,max=50)])
    address = StringField('Address', validators=[DataRequired(), Length(min=3,max=50)])
    signature_dish = QuerySelectField('Signature Dish', query_factory=lambda: SignatureDish.query, allow_blank=True)


class SignatureDishForm(FlaskForm):
    name = StringField('Dish Name', validators=[DataRequired(), Length(min=3,max=50)])
    price = FloatField('Price', validators=[DataRequired(), Length(min=3,max=50)])