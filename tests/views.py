import flask
import flask_login
from Project.toolbox import config_page
import os

def render_tests():
    return flask.render_template("tests.html", avatar_filepath = os.path.join("user_profile","static","user_avatars", flask_login.current_user.avatar))