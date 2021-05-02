from flask import Flask, render_template, url_for
from forms import SignupForm, LoginForm



app = Flask(__name__)

app.config['SECRET_KEY'] = '8675ignl1'

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
    return render_template('home.html', restaurants=restaurant_sample)

@app.route('/signup', methods =['GET','POST'])
def signup():
    form = SignupForm()
    return render_template('signup.html', form=form, title='Signup')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form=form)

@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html')

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/about')
def about():
    return render_template('about.html')




if __name__ == '__main__':
    app.run(debug=True)