from flask import render_template, url_for, flash, redirect
from restaurant_site import app
from restaurant_site.forms import SignupForm, LoginForm, RestaurantForm
from restaurant_site.models import User, Restaurant
from restaurant_site import db
from flask_bcrypt import Bcrypt 


bcrypt = Bcrypt()


@app.route('/')
def home():
    restaurants = Restaurant.query.all()
    return render_template('home.html', restaurants=restaurants)

@app.route('/signup', methods =['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password= hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account Created')
        return redirect(url_for('home'))

    return render_template('signup.html', form=form, title='Signup')

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            bcrypt.check_password_hash(user.password, form.password.data)
            flash('Successfully logged in')
            return redirect(url_for('home'))
    return render_template('login.html', title = 'Login', form=form)

@app.route('/restaurant', methods =['GET', 'POST'])
def restaurant():
    form = RestaurantForm()
    if form.validate_on_submit():
        store = Restaurant(name=form.name.data, address=form.address.data)
        db.session.add(store)
        db.session.commit()
        flash('Store Created')
        return redirect(url_for('home'))
    return render_template('restaurant.html', title = 'Restaurants Form', form=form)

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/about')
def about():
    return render_template('about.html')
