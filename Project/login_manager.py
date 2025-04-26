import flask_login
from .settings import project

from registration.models import User

project.secret_key ="141242153252652"
login_maneger = flask_login.LoginManager(app = project)

@login_maneger.user_loader
def load_user(id):
    return User.query.get(id)