from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import  relationship

from contract.db.association import student_course
from contract.db.db import Base


# Визначення моделей даних (таблиць) за допомогою класів
class OrmCourses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Встановлення відношення "один до багатьох" з таблицею Employee
    students = relationship('OrmStudent', secondary=student_course, back_populates='courses')