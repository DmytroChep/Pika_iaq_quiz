import flask
from flask import render_template, redirect
from flask_login import current_user
import os
from tests.models import *

def render_core():
    user = current_user
    
    if current_user.is_authenticated:
        tests_from_user = reversed(Quiz.query.filter_by(author_id=current_user.id).all())
        all_tests = reversed(Quiz.query.all())

        return render_template(
            template_name_or_list='home.html', 
            avatar_filepath=os.path.join("user_profile", "static", "user_avatars", user.avatar), 
            tests_from_user=tests_from_user, 
            all_tests = all_tests
        )
    else:
        return redirect("registration")

