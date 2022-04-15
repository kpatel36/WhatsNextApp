from flask import Flask
from config import Config

from .auth.routes import auth
from .user_lists.user_lists_routes import user_lists
from .models import db, login
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origin=(["*"]))

app.config.from_object(Config)

app.register_blueprint(auth)
app.register_blueprint(user_lists)

db.init_app(app)
migrate = Migrate (app,db)

# set up my login manager
login.init_app(app)
login.login_view = 'auth.login'
login.login_message = 'Please sign in to see this page'
login.login_message_category='info'


from . import routes # from app folder (that we're currently in), import the routes file
from . import models            #<!-- <a href="{{ url_for(user_lists.userProfile, username=user.username) }}" class="btn btn-block btn-outline-primary">View Profile</a> -->