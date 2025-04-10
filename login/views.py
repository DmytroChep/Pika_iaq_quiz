import flask
import flask_login
from regestration.models import User

def render_login():
    if flask.request.method == 'POST':
        for user in User.query.filter_by(login = flask.request.form["username"]):
            if user.password == flask.request.form["password"] and user.login == flask.request.form["username"]:
                flask_login.login_user(user)
                return flask.redirect("/main2/")

            else:
                return flask.redirect("/login2")

    return flask.render_template(template_name_or_list= "login.html")