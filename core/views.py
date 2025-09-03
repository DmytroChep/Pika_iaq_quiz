import flask
from flask import render_template, redirect
from flask_login import current_user

def render_core():
    if current_user.is_authenticated:
        return render_template(template_name_or_list= 'home.html')
    else:
        return redirect("registration")
        return redirect("registration")