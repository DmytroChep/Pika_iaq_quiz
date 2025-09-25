import flask
import flask_login
from Project.toolbox import config_page
import os
import json
from flask_login import current_user
from .models import Question, Quiz, DATABASE, activeQuiz
from datetime import datetime
from werkzeug.utils import secure_filename
from flask_socketio import join_room, leave_room, emit
import io, base64
from Project.settings import socketio
import random


def save_test():
    print(flask.request.form)     
    print(flask.request.files)
    questions_list = []
    quiz_name = flask.request.form["quiz_name"]
    quiz_photo = None
    if 'quiz_avatar' in flask.request.files:
        file = flask.request.files['quiz_avatar']
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            filepath = os.path.join("tests", "static", "quiz_avatars", filename)

            file.save(filepath)
            quiz_photo = filename

    print(quiz_photo)


    quiz_object = Quiz(
        name=quiz_name,
        photo = quiz_photo,
        author_id=flask_login.current_user.id
    )
    DATABASE.session.add(quiz_object)
    DATABASE.session.commit()
    for count in range(len(json.loads(flask.request.form["questions"]))):
        question_now = json.loads(flask.request.form["questions"])[str(count + 1)]

        question_object = Question(
            quiz_id=quiz_object.id,
            question_name=question_now["questionTitle"],
            answer_name1=question_now["answer1"]["title"],
            answer_name2=question_now["answer2"]["title"],
            corrrect_answers = flask.request.form[f"correctAnswers{count + 1}"]
        )

        try:
            question_object.answer_name3 = question_now["answer3"]["title"]
            question_object.answer_name4 = question_now["answer4"]["title"]
        except:
            pass
        


        string_flask_files = str(flask.request.files)

        if f"questionImage{count + 1}" in string_flask_files:
            file = flask.request.files[f"questionImage{count + 1}"]

            filename = secure_filename(file.filename)
            filepath = os.path.join("tests", "static", "question_images", filename)

            file.save(filepath)

            question_object.question_image = filename



        if f"answerImage1_{count + 1}" in string_flask_files:
            print("1")
            file = flask.request.files[f"answerImage1_{count + 1}"]

            filename = secure_filename(file.filename)
            filepath = os.path.join("tests", "static", "answer_images", filename)

            file.save(filepath)

            question_object.answer_image1 = filename
        if f"answerImage2_{count + 1}" in string_flask_files:
            print("2")
            file = flask.request.files[f"answerImage2_{count + 1}"]

            filename = secure_filename(file.filename)
            filepath = os.path.join("tests", "static", "answer_images", filename)

            file.save(filepath)

            question_object.answer_image2 = filename
        if f"answerImage3_{count + 1}" in string_flask_files:
            print("3")
            file = flask.request.files[f"answerImage3_{count + 1}"]

            filename = secure_filename(file.filename)
            filepath = os.path.join("tests", "static", "answer_images", filename)

            file.save(filepath)

            question_object.answer_image3 = filename
        if f"answerImage4_{count + 1}" in string_flask_files:
            print("4")
            file = flask.request.files[f"answerImage4_{count + 1}"]

            filename = secure_filename(file.filename)
            filepath = os.path.join("tests", "static", "answer_images", filename)

            file.save(filepath)

            question_object.answer_image4 = filename

        questions_list.append(question_object)

    DATABASE.session.add_all(questions_list)
    DATABASE.session.commit()

    return {"status": "good"}

def render_tests():
    if current_user.is_authenticated:
        print(datetime.now().strftime("%Y.%m.%d"))
        return flask.render_template("tests.html", avatar_filepath=os.path.join("..", "user_profile", "static", "user_avatars", flask_login.current_user.avatar))
    else:
        return flask.redirect("registration")
    

def render_tests_passing(test_id):
    test = Quiz.query.get(ident = test_id)

    
    return flask.render_template("test_passing.html", test = test)


@socketio.on("createQuiz")
def createQuiz(data):
    print(f"user {data['user']} connected to quiz {data['quiz']}")

    all_active_quizes = activeQuiz.query.all()
    all_quiz_numbers = []
    for quiz in all_active_quizes:
        all_quiz_numbers.append(quiz.quiz_number)

    random_num = random.randint(100000, 999999)
    
    while True:
        if random_num in all_quiz_numbers:
            random_num =  random.randint(100000, 999999)
            break
        else:
            break

    active_quiz = activeQuiz(
        quiz_number=random_num,
        quiz_id=data["quiz"],
        users=[flask_login.current_user] 
    )

    DATABASE.session.add(active_quiz)
    DATABASE.session.commit()

@socketio.on('disconnect')
def handle_disconnect(*args, **kwargs):
    client = flask_login.current_user
    print(client)

    all_quizes = activeQuiz.query.all()

    for quiz in all_quizes:
        print(quiz.users)
        if quiz.users != []:
            if quiz.users[0] == client:
                DATABASE.session.delete(quiz)
                emit('teacherGetOut')
            else:
                client.active_quiz_id = None
                emit('userGetOut')

        DATABASE.session.commit()  
    print(all_quizes)