import flask
import flask_login
from Project.db import DATABASE

def render_user_profile():
    if flask.request.method == "POST":
        user = flask_login.current_user
        user.login = flask.request.form["username"]
        user.email = flask.request.form["gmail"]
        user.password = flask.request.form["password"]
        DATABASE.session.commit()
    if flask_login.current_user.is_authenticated:
        return flask.render_template("profile.html")
    else:
        return flask.redirect("/registration")