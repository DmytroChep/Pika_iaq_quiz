from Project.db import DATABASE
import os
import flask_login
from sqlalchemy.orm import relationship


class User(DATABASE.Model, flask_login.UserMixin):
    __tablename__ = "users"
    
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    login = DATABASE.Column(DATABASE.String(50), nullable=False)
    email = DATABASE.Column(DATABASE.String(256), nullable=False)
    password = DATABASE.Column(DATABASE.String(50), nullable=False)
    is_teacher = DATABASE.Column(DATABASE.Boolean, default=False, nullable=False)
    avatar = DATABASE.Column(DATABASE.String, nullable=True, default="standart_avatar.png")
    
    # Явное отношение с back_populates
    quizes = relationship("Quiz", back_populates="author")
    
    def __repr__(self) -> str:
        return f"user : {self.login}"