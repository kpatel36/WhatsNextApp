from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from uuid import uuid4

from flask_login import LoginManager, UserMixin

# create instance of login manager
login = LoginManager()

# query db for user - necesaary func for login manager
@login.user_loader
def load_user(user_id): #accepts user_id as input and returns db query for that user id
    return User.query.get(user_id)

# follower-following table
# standalone table for user-follower-following relationship, but not its own entity/object
followers = db.Table(
    'followers',
    db.Column('follower_id', db.String, db.ForeignKey('user.id')),
    db.Column('user_id', db.String, db.ForeignKey('user.id')),

)




class User(db.Model,UserMixin):
    # lay out columns like would in SQL create table query
    # column_name = db.Column(db.DataType(<options>), constraints)
    id = db.Column(db.String(50),primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    short_bio = db.Column(db.String(160))
    long_bio = db.Column(db.String(250))
    password = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    followed = db.relationship(
        'User',
        secondary=followers,  #secondary way relationship is defined will be 'followers'
        primaryjoin=(followers.c.follower_id==id), # c='column'; primary join will be used when we try to get all of the users this user is following 
        secondaryjoin=(followers.c.user_id==id), # secondary join is the one needed to find all users who follow this user
        backref = db.backref('followers')
    )

    def __init__ (self, username, email, password, first_name="", last_name=""):
        self.username = username
        self.email = email.lower()
        self.password = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name 
        self.id = str(uuid4())

    def follow(self, u):
        """ expects user object, follows that user """
        self.followed.append(u)
        db.session.commit()
    
    def unfollow(self, u):
        """ expect user object, unfollows that user"""
        self.followed.remove(u)
        db.session.commit()


    