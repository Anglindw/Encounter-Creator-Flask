from flask import Flask
from config import Config
from flask_migrate import Migrate
from .models import db, User, Team
from .auth.routes import auth
from .teams.routes import team
from .monsters.routes import monster
from .fight.routes import fight
from flask_login import LoginManager
app = Flask(__name__)

app.config.from_object(Config)

login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(auth)
app.register_blueprint(team)
app.register_blueprint(monster)
app.register_blueprint(fight)

db.init_app(app)
migrate = Migrate(app, db)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

from . import routes
from . import models