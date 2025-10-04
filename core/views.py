import flask
from flask import render_template, redirect
from flask_login import current_user
import os
from tests.models import *
from registration.models import *
from Project.settings import socketio
import flask_login


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

@socketio.on("connectQuiz")
def connectQuiz(data):
    client = User.query.filter_by(id = flask_login.current_user.id).first()

    quiz = activeQuiz.query.filter_by(quiz_number=data["quizNumber"]).first()
    
    client.active_quiz = quiz
    # quiz.users.append(client)
    DATABASE.session.commit()
    # DATABASE.session.commit()
    
    print(f"User {client} added to quiz {quiz}")