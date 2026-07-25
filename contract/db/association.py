
from sqlalchemy import Table, Column, Integer, ForeignKey #для створення таблиці
from contract.db.db import Base # Base — базовий клас, потрібен щоб прив'язати таблицю

student_course = Table(
    'student_course',   # назва таблиці в БД
    Base.metadata,            # реєструємо таблицю
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True), # колонка з id студента, зовнішній ключ на students.id
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True),   # колонка з id курсу
)