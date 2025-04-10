import flask
from .models import User
from Project.settings import DATABASE

def render_registration():
    if flask.request.method == 'POST':
        user = User(login = flask.request.form['name'], 
                    password = flask.request.form["password"], 
                    email = flask.request.form["email"], 
                    password_confirm = flask.request.form["password_confirm"],
                    is_teacher = False
                    )
               
        try:
            DATABASE.session.add(user)
            DATABASE.session.commit()
            return flask.redirect("/core/")
        except:
            print(":hkeopihnwjiouewh")
            return 'ERROR'
    return flask.render_template(template_name_or_list= "registration.html")

