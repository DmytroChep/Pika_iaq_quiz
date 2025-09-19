import flask
import flask_login
from Project.db import DATABASE
from werkzeug.utils import secure_filename
import os
from Project.settings import project



def render_user_profile():
    user = flask_login.current_user
    if flask.request.method == "POST":
        if 'avatar' in flask.request.files and flask.request.files["avatar"]:
            load_avatar = flask.request.files["avatar"]
            filename = secure_filename(load_avatar.filename)
            load_avatar.save(os.path.abspath(os.path.join("user_profile","static","user_avatars", filename)))
            user.avatar = filename
        user.login = flask.request.form["username"]
        user.email = flask.request.form["gmail"]
        user.password = flask.request.form["password"]
        DATABASE.session.commit()
    if flask_login.current_user.is_authenticated:
        print(user.avatar)
        return flask.render_template("profile.html", avatar_filepath = os.path.join("user_profile","static","user_avatars", user.avatar))
    else:
        return flask.redirect("/registration")


