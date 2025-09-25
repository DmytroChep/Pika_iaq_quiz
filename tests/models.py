from sqlalchemy.orm import relationship
from Project.db import DATABASE
from datetime import datetime

class Quiz(DATABASE.Model):
    __tablename__ = "quizes"
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    name = DATABASE.Column(DATABASE.String(50))
    photo = DATABASE.Column(DATABASE.String)
    
    author_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey('users.id'))
    
    author = relationship("User", back_populates="quizes")

    date_creation = DATABASE.Column(DATABASE.String, default = datetime.now().strftime("%Y.%m.%d"))
    
    questions = relationship("Question", backref="quiz")
    active_quiz = relationship("activeQuiz", backref="quiz")

class Question(DATABASE.Model):
    __tablename__ = "questions"
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    
    corrrect_answers = DATABASE.Column(DATABASE.String(50))

    quiz_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey('quizes.id'))
    
    question_name = DATABASE.Column(DATABASE.String(50))
    question_image = DATABASE.Column(DATABASE.String) 
    

    answer_name1 = DATABASE.Column(DATABASE.String(50))
    answer_image1 = DATABASE.Column(DATABASE.String)
    
    answer_name2 = DATABASE.Column(DATABASE.String(50))
    answer_image2 = DATABASE.Column(DATABASE.String)
    
    answer_name3 = DATABASE.Column(DATABASE.String(50), nullable=True)
    answer_image3 = DATABASE.Column(DATABASE.String, nullable=True)
    
    answer_name4 = DATABASE.Column(DATABASE.String(50), nullable=True)
    answer_image4 = DATABASE.Column(DATABASE.String, nullable=True)


class activeQuiz(DATABASE.Model):
    __tablename__ = "activeQuiz"
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    quiz_number = DATABASE.Column(DATABASE.Integer)
    quiz_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey('quizes.id'))
    
    users = relationship("User", back_populates="active_quiz")  