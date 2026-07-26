from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import  relationship    # relationship — для визначення зв'язку між ORM

from contract.db.association import student_course  # імпорт асоціативної таблиці, через яку реалізується зв'язок many-to-many
from contract.db.db import Base         #імопрт класу для наслідування

# Визначення моделей даних (таблиць) за допомогою класів
class OrmStudent(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    courses = relationship('OrmCourses', secondary=student_course, back_populates='students')  # зв'язок many-to-many з моделлю OrmCourses через асоціативну таблицю student_course;

    def __repr__(self):         #для виводу значень, а не об'єкту
        return f'OrmStudent:: id: {self.id}, name: {self.name}, age: {self.age}'