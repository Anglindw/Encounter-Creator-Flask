from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password =  db.Column(db.String(300), nullable=False)
    post = db.relationship('Team', backref='Discover', lazy = True)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False,  )
    tclass = db.Column(db.String(), nullable=False, )
    level = db.Column(db.Integer, nullable=False,)
    challenge_score = db.Column(db.Float(2), nullable=False)
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, tclass, level, challenge_score, user_id):
        self.name = name
        self.tclass = tclass
        self.level = level
        self.challenge_score = challenge_score
        self.user_id = user_id


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def  delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class Monsters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable= False, unique=True)
    challenge_rating = db.Column(db.Numeric(10,2), nullable=False)
    hit_points = db.Column(db.Integer, nullable=False)
    armor_class = db.Column(db.Integer, nullable = False)

    def __init__(self, name, challenge_rating, hit_points, armor_class):
        self.name = name
        self.challenge_rating = challenge_rating
        self.hit_points = hit_points
        self.armor_class = armor_class

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def  delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    


