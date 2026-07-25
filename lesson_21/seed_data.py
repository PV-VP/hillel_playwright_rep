from sqlalchemy.sql.expression import select

from contract.db.orm_courses_table import OrmCourses
from contract.db.orm_student_table import OrmStudent
from contract.db.db import Base, engine, session
from faker import Faker
import random

f = Faker()

"""Створення моделі даних: Створіть просту модель даних для системи управління студентами.
Модель може містити таблиці для студентів, курсів та їх відношень.
Кожен студент може бути зареєстрований на декілька курсів.
Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів."""

def seed_students_orm():
    #Додавання нового студента
    new_student = [OrmStudent(name=f.name(), age=random.choice(range(16, 60))) for k in range(20)] #створюєм 20 рандомних студентів з рандомним віком
    session.add_all(new_student)   #додаєм студента .add_all
    session.commit()

def seed_courses_orm():
    courses_names = [
        'Python для початківців',
        'Основи QA та тестування ПЗ',
        'SQL та бази даних',
        'Автоматизоване тестування з Playwright',
        'Основи DevOps',
    ]
    new_courses = [OrmCourses(name=name) for name in courses_names]
    session.add_all(new_courses)
    session.commit()

def seed_student_course_links():
    # отримуємо всіх студентів і всі курси з бази
    students = session.scalars(select(OrmStudent)).all()
    courses = session.scalars(select(OrmCourses)).all()
    for student in students:
        # кожному студенту призначаємо рандомну кількість курсів (від 1 до 3)
        num_courses = random.randint(1, 3)
        # рандомно обираємо унікальні курси без повторів
        student.courses = random.sample(courses, num_courses)

    session.commit()

if __name__ == '__main__': #перевірка чи ми в файлі для того щоб не створити знов студентів і курси
    seed_students_orm()
    seed_courses_orm()
    seed_student_course_links()