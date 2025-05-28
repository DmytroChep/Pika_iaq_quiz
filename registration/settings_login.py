import flask
import flask_login
from .models import User

def login():
    for user in User.query.filter_by(login = flask.request.form["username"]):
        if user.password == flask.request.form["password"]:
            flask_login.login_user(user)
            print("sucsessfully login user:", flask.request.form["username"])
            return None
        else:
            print("failed to login")
            return "failed to login"