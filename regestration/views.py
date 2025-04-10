import flask
from .models import User
from Project.settings import DATABASE

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
            return flask.redirect("/core/")
        except Exception as e:
            print(f"Ошибка при добавлении пользователя в базу данных: {e}")
            return 'ERROR'
    return flask.render_template(template_name_or_list= "registration.html")

