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
            #login()
            
               
            
            
            return flask.redirect("/login")
        except Exception as e:
            print(f"Ошибка при добавлении пользователя в базу данных: {e}")
            return 'ERROR'
    return flask.render_template(template_name_or_list= "registration.html")

def render_authorization():
    
    if flask.request.method == "POST":
        print ("wqdwqdfqwfdwqfwqfqfwqf")
        username_form = flask.request.form['username'], 
        password_form = flask.request.form["password"]

        list_users = User.query.all()
        for user in list_users:
            if User.login == username_form and User.password == password_form:
        #        print ("wqdwqdfqwfdwqfwqfqfwqf")
                flask_login.login_user(user)
    if not flask_login.current_user.is_authenticated:
        return flask.render_template("login.html")
    else:
        return flask.redirect("/")

def render_login():
    if flask.request.method == "POST":
        login()
        return flask.redirect("/")
    
    return flask.render_template(template_name_or_list= "login.html")