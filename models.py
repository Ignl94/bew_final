from __main__ import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    address = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"User('{self.name}', {self.address}')"