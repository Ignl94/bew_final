from flask import render_template, url_for, flash, redirect
from restaurant_site import app
from restaurant_site.forms import SignupForm, LoginForm, RestaurantForm, ReviewForm
from restaurant_site.models import User, Restaurant, Reviews
from restaurant_site import db
from flask_bcrypt import Bcrypt 
from flask_login import login_user, current_user, logout_user, login_required


bcrypt = Bcrypt()


@app.route('/')
def home():
    restaurants = Restaurant.query.all()
    reviews = Reviews.query.all()
    return render_template('home.html', restaurants=restaurants, reviews=reviews)

@app.route('/signup', methods =['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password= hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account Created')
        return redirect(url_for('login'))

    return render_template('signup.html', form=form, title='Signup')

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Successfully logged in')
            return redirect(url_for('home'))
    return render_template('login.html', title = 'Login', form=form)

@app.route('/restaurant', methods =['GET', 'POST'])
@login_required
def restaurant():
    form = RestaurantForm()
    if form.validate_on_submit():
        store = Restaurant(name=form.name.data, address=form.address.data)
        db.session.add(store)
        db.session.commit()
        flash('Store Created')
        return redirect(url_for('home'))
    return render_template('restaurant.html', title = 'Restaurants Form', form=form)

@app.route('/review',methods=['GET','POST'])
@login_required
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        review = Reviews(review=form.review.data)
        db.session.add(review)
        db.session.commit()
        flash('Review Created')
        return redirect(url_for('home'))
    return render_template('review.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
