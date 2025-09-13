from sqlalchemy.orm import relationship, relation
from Project.db import DATABASE
class Quiz():
    __tablename__ = "quizes"

    questions = relationship("Question", backref="quiz")
    name = DATABASE.Column(DATABASE.String(50))
    photo = DATABASE.Column(DATABASE.String)
    author = relationship("User", backref= "quiz")

class Question():
    __tablename__ = "question"

    quiz_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey('quizs.quizs_id'))
    quiz = DATABASE.relationship('Quiz')

    question_name = DATABASE.Column(DATABASE.String(50))
    qustion_image = DATABASE.Column(DATABASE.String)

    first_answer_name1 = DATABASE.Column(DATABASE.String(50))
    first_answer_image1 = DATABASE.Column(DATABASE.String)

    first_answer_name2 = DATABASE.Column(DATABASE.String(50))
    first_answer_image2 = DATABASE.Column(DATABASE.String)

    first_answer_name3 = DATABASE.Column(DATABASE.String(50), nullable = True)
    first_answer_image3 = DATABASE.Column(DATABASE.String, nullable = True)

    first_answer_name4 = DATABASE.Column(DATABASE.String(50), nullable = True)
    first_answer_image4 = DATABASE.Column(DATABASE.String, nullable = True)