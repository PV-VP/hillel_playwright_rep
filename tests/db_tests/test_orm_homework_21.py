import random
import pytest

from faker import Faker
from sqlalchemy.sql.expression import select, update

from contract.db.db import session
from contract.db.orm_courses_table import OrmCourses
from contract.db.orm_student_table import OrmStudent

f = Faker()

@pytest.fixture()   #фікстури, щоб не дублювати код, предаєм як аргумент в фунцію
def random_student_id():
    students_id = select(OrmStudent.id)  # будуєм запит де всі id студентів
    res = session.scalars(students_id).all()  # виконуєм запит отримуєм всі
    random_student_id = random.choice(res)  # берем рандомний. Для того щоб отримувати реальні id
    return random_student_id

@pytest.fixture()
def random_course_id():
    course_id = select(OrmCourses.id)
    res = session.scalars(course_id).all()
    random_course_id = random.choice(res)
    return random_course_id

"""Виконання базових операцій: Напишіть програму, 
яка додає нового студента до бази даних та додає його до певного курсу. 
Переконайтеся, що ці зміни коректно відображаються у базі даних."""
@pytest.mark.add    #марка для запуску тесту
def test_add_student_course_orm(random_course_id):
    # Додавання нового студента
    new_student = OrmStudent(name=f.name(), age=random.choice(range(16, 60))) #створюєм 1  студентів з рандомним віком
    session.add(new_student)   #додаєм студента .add
    session.commit()
    # отримання інформації про потрібний курс

    course_query = select(OrmCourses).where(OrmCourses.id == random_course_id)  #запит який отримує курс
    result = session.scalars(course_query).first()    # виконуєм запит/.first() бо очікуємо ОДИН результат

    new_student.courses.append(result)# записуємо студента на курс: додаємо курс у список student.courses
    session.commit()

    upd_student = session.scalars(select(OrmStudent).where(OrmStudent.id == new_student.id)).first() # повторно робимо запит до БД і дістаємо цього ж студента за його id
    assert result in upd_student.courses    # перевіряємо: чи є доданий курс (result) у списку курсів студента після перечитування з БД
    print(upd_student, upd_student.courses)

"""Запити до бази даних: Напишіть запити до бази даних, 
які повертають інформацію про студентів, зареєстрованих на певний курс, 
або курси, на які зареєстрований певний студент."""

@pytest.mark.info   #марка для запуску тесту
def test_info_students_on_course(random_course_id):

    info_students_query = select(OrmCourses).where(OrmCourses.id == random_course_id)
    result = session.scalars(info_students_query).first()
    print(result.students)

@pytest.mark.info
def test_info_courses_of_students(random_student_id):
    info_course_query = select(OrmStudent).where(OrmStudent.id == random_student_id)    #умови що вивести
    result = session.scalars(info_course_query).first() #виконуєм запит
    print(result.courses)

"""Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси,
 а також видалення студентів з бази даних."""
@pytest.mark.update
def test_upd_student(random_student_id):

    student_query = select(OrmStudent).where(OrmStudent.id == random_student_id)   # запит щоб дістати старі значення для очік результату
    exp_student_res = session.scalars(student_query).first()

    name_student = exp_student_res.name     #очік ім'я
    age = exp_student_res.age               #очік вік

    exp_name_student = f.first_name() # нові значення
    exp_age_student = random.choice(range(20, 40))


    student_upd_query = (update(OrmStudent).where(OrmStudent.id == random_student_id)       # запит на оновлення студента за id
                          .values(name=exp_name_student, age=exp_age_student))
    session.execute(student_upd_query)  #виконуєм запит
    session.commit()    #комітим зіміни

    ar_student_res = session.scalars(select(OrmStudent).where(OrmStudent.id == random_student_id)).first()     # перечитуємо студента з бази, щоб перевірити, що зміни реально збереглись

    assert ar_student_res.name != name_student
    assert ar_student_res.age != age
    assert ar_student_res.name == exp_name_student
    assert ar_student_res.age == exp_age_student
    assert ar_student_res.id == random_student_id
@pytest.mark.delete
def test_del_student(random_student_id):
    student_to_del_query = select(OrmStudent).where(OrmStudent.id == random_student_id)
    student = session.scalars(student_to_del_query).first()   # виконуємо запит і отримуємо сам об'єкт

    session.delete(student)
    session.commit()

    check_query = select(OrmStudent).where(OrmStudent.id == random_student_id)
    check_result = session.scalars(check_query).first()
    assert check_result is None