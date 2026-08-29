import random
import pytest

from faker import Faker
from sqlalchemy.sql.expression import select, update

from contract.db.db import session
from contract.db.orm_courses_table import OrmCourses
from contract.db.orm_student_table import OrmStudent
import allure

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


@allure.epic('Студенти')
@allure.feature('Студенти та курси (ORM) - додавання/видалення, отримання інформації про курс/студента')
@allure.link(url='jira-board/ed-01', name='ed-01')
@pytest.mark.students_crud
class TestStudents:
    """Виконання базових операцій: Напишіть програму,
    яка додає нового студента до бази даних та додає його до певного курсу.
    Переконайтеся, що ці зміни коректно відображаються у базі даних."""
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Цей тест додає студента на курс і перевіряє чи додавання відбулось')
    @allure.story('Реєстрація на курс')
    @allure.title('Додавання студента до курсу')
    @pytest.mark.add  # марка для запуску тесту
    def test_add_student_course_orm(self,random_course_id):

        with allure.step('Додати нового студента'):
            new_student = OrmStudent(name=f.name(), age=random.choice(range(16, 60)))
            session.add(new_student)
            session.commit()

        with allure.step(f'Отримати курс за id {random_course_id} і записати студента на нього'):
            course_query = select(OrmCourses).where(OrmCourses.id == random_course_id)
            result = session.scalars(course_query).first()
            new_student.courses.append(result)
            session.commit()

        with allure.step('Перевірити, що курс з’явився у списку курсів студента'):
            upd_student = session.scalars(select(OrmStudent).where(OrmStudent.id == new_student.id)).first()
            assert result in upd_student.courses
            print(upd_student, upd_student.courses)

    """Запити до бази даних: Напишіть запити до бази даних,
    які повертають інформацію про студентів, зареєстрованих на певний курс,
    або курси, на які зареєстрований певний студент."""

    @allure.severity(allure.severity_level.MINOR)
    @allure.description('Цей тест отримує інформацію про студента і його курс')
    @allure.story('Перегляд інформації')
    @allure.title('Отримання інформації про студента, зареєстрованих на певний курс')
    @pytest.mark.info  # марка для запуску тесту
    def test_info_students_on_course(self, random_course_id):
        with allure.step(f'Отримати курс за id {random_course_id} та список студентів на ньому'):
            info_students_query = select(OrmCourses).where(OrmCourses.id == random_course_id)
            result = session.scalars(info_students_query).first()
            print(result.students)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Цей тест отримує інформацію про курс і студентов на ньому')
    @allure.story('Перегляд інформації')
    @allure.title('Отримання інформації про курси на які зареєстрований певний студент')
    @pytest.mark.info # марка для запуску тесту
    def test_info_courses_of_students(self,random_student_id):
        with allure.step(f'Отримати курси за id {random_student_id}'):
            info_course_query = select(OrmStudent).where(OrmStudent.id == random_student_id)    #умови що вивести
            result = session.scalars(info_course_query).first() #виконуєм запит
            print(result.courses)

    """Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси,
     а також видалення студентів з бази даних."""
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.description('Цей тест оновлює інформацію про студента і перевіряє її')
    @allure.story('Зміна даних студента')
    @allure.title('Оновлення данних про студента')
    @pytest.mark.update
    def test_upd_student(self,random_student_id):
        with allure.step('Отримуєм данні про студента'):
            student_query = select(OrmStudent).where(OrmStudent.id == random_student_id)   # запит щоб дістати старі значення для очік результату
            exp_student_res = session.scalars(student_query).first()

            name_student = exp_student_res.name     #очік ім'я
            age = exp_student_res.age               #очік вік

            exp_name_student = f.first_name() # нові значення
            exp_age_student = random.choice(range(20, 40))

        with allure.step('Змінюєм данні'):
            student_upd_query = (update(OrmStudent).where(OrmStudent.id == random_student_id)       # запит на оновлення студента за id
                                  .values(name=exp_name_student, age=exp_age_student))
            session.execute(student_upd_query)  #виконуєм запит
            session.commit()    #комітим зіміни

        with allure.step('Перевіряєм змінені данні'):
            ar_student_res = session.scalars(select(OrmStudent).where(OrmStudent.id == random_student_id)).first()  # перечитуємо студента з бази, щоб перевірити, що зміни реально збереглись
            assert ar_student_res.name != name_student
            #assert ar_student_res.age != age
            assert ar_student_res.age == age #тест завален спеціально для виводу в алюр
            assert ar_student_res.name == exp_name_student
            assert ar_student_res.age == exp_age_student
            assert ar_student_res.id == random_student_id

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Цей тест видаляє студента і перевіряє чи видалення відбулось')
    @allure.story('Зміна даних студента')
    @allure.title('Видалення студента')
    @pytest.mark.delete
    def test_del_student(self, random_student_id):
        with allure.step(f'Отримати та видалити студента з id: {random_student_id}'):
            student_to_del_query = select(OrmStudent).where(OrmStudent.id == random_student_id)
            student = session.scalars(student_to_del_query).first()
            session.delete(student)
            session.commit()

        with allure.step('Перевірка видалення студента'):
            check_query = select(OrmStudent).where(OrmStudent.id == random_student_id)
            check_result = session.scalars(check_query).first()
            assert check_result is None