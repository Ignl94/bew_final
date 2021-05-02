from flask import Flask, render_template, url_for, flash, redirect
from forms import SignupForm, LoginForm, RestaurantForm
from flask_sqlalchemy import SQLAlchemy 




app = Flask(__name__)

app.config['SECRET_KEY'] = '8675ignl1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
from models import User, Restaurant



restaurant_sample = [
    {
        'name': 'Harolds',
        'address': '123 Street',
        'signature_dish': 'Spaghetti'
    },
    {
        'name': 'Marthas',
        'address': '345 Lane',
        'signature_dish': 'Ice Cream'
    }
]

@app.route('/')
def home():
    restuarants = Restuarant.query.all()
    return render_template('home.html', restaurants=restaurants)

@app.route('/signup', methods =['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash('Account Created')
        return redirect(url_for('home'))

    return render_template('signup.html', form=form, title='Signup')

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Successfully logged in')
        return redirect(url_for('home'))
    return render_template('login.html', title = 'Login', form=form)

@app.route('/restaurant')
def restaurant():
    form = RestaurantForm()
    return render_template('restaurant.html', title = 'Restaurants Form', form=form)

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/about')
def about():
    return render_template('about.html')




if __name__ == '__main__':
    app.run(debug=True)