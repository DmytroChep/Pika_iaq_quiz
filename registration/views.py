import flask
from .models import User
from Project.db import DATABASE
from registration.settings_login import login

def render_registration():
    if flask.request.method == 'POST':
        user = User(
                   
                    login = flask.request.form['login'], 
                    password = flask.request.form["password"], 
                    email = flask.request.form["email"], 
                    is_teacher = False
                    )
               
        try:
            DATABASE.session.add(user)
            DATABASE.session.commit()
            login()
            return flask.redirect("/login/")
        except Exception as e:
            print(f"Ошибка при добавлении пользователя в базу данных: {e}")
            return 'ERROR'
    return flask.render_template(template_name_or_list= "registration.html")



def render_login():
    if flask.request.method == "POST":
        login()
        return flask.redirect("/")
    
    return flask.render_template(template_name_or_list= "login.html")