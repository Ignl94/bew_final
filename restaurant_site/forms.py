from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, TextField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, ValidationError
from restaurant_site.models import Restaurant, User




class SignupForm(FlaskForm):
    username = StringField('Enter Username', validators=[DataRequired(), Length(min=3,max=20)])
    password = StringField('Enter Password', validators=[DataRequired(), Length(min=3,max=50)])
    submit = SubmitField('Signup')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("User already exists")


class LoginForm(FlaskForm):
    username = StringField('Enter Username', validators=[DataRequired(), Length(min=3,max=20)])
    password = PasswordField('Enter Password', validators=[DataRequired(), Length(min=3,max=350)])
    submit = SubmitField('Login')


class RestaurantForm(FlaskForm):
    name = StringField('Restaurant Name', validators=[DataRequired(),Length(min=3,max=20)])
    address = StringField('Address', validators=[DataRequired(), Length(min=3,max=50)])
    submit = SubmitField('Submit')


class ReviewForm(FlaskForm):
    review = TextField('Leave Review', validators=[DataRequired(), Length(min=3,max=500)])
    restaurant = QuerySelectField('Restaurant', query_factory=lambda: Restaurant.query)
    submit = SubmitField('Submit Review')