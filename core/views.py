import flask
from flask import render_template, redirect
from flask_login import current_user
import os

def render_core():
    user = current_user
    # if current_user.is_authenticated:
    #     return render_template(template_name_or_list= 'home.html', avatar_filepath = os.path.join("user_profile","static","user_avatars", user.avatar))
    # else:
    return redirect("registration")
