import flask , flask_login 
from .models import User
from Project.db import DATABASE
from registration.settings_login import login

def render_registration():
    if flask.request.method == 'POST':
        user = User(
                   
                    login = flask.request.form['username'], 
                    password = flask.request.form["password"], 
                    email = flask.request.form["email"], 
                    is_teacher = False
                    )
               
        try:
            DATABASE.session.add(user)
            DATABASE.session.commit()
            
               
            
            
            return flask.redirect("/login")
        except Exception as e:
            print(f"Ошибка при добавлении пользователя в базу данных: {e}")
            return 'ERROR'
    return flask.render_template(template_name_or_list= "registration.html")

def render_authorization():
    
    if flask.request.method == "POST":
        username_form = flask.request.form['username'], 
        password_form = flask.request.form["password"]

        list_users = User.query.all()
        for user in list_users:
            if user.login == username_form and user.password == password_form:
                print(user)
                flask_login.login_user(user)
                return flask.redirect("/")

        return flask.render_template("login.html")
        

def render_login():
    if flask.request.method == "POST":
        username_form = flask.request.form['username']
        password_form = flask.request.form["password"]

        list_users = User.query.all()
        print(list_users)
        print(username_form, password_form)
        for user in list_users:
            if user.login == username_form and user.password == password_form:
                print(user)
                flask_login.login_user(user)
                return flask.redirect("/")

        return flask.render_template("login.html")
    
    return flask.render_template(template_name_or_list= "login.html")