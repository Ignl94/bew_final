from restaurant_site import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(350), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    address = db.Column(db.String(50), nullable=False, unique=True)
    reviews = db.relationship('Reviews')

    def __repr__(self):
        return f"User('{self.name}', {self.address}')"

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))