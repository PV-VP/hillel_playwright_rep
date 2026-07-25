from contract.db.db import Base, engine
# Base — базовий клас, від якого наслідуються всі ORM
# engine — з'єднання з базою даних
from contract.db.orm_student_table import OrmStudent
from contract.db.orm_courses_table import OrmCourses

Base.metadata.create_all(engine)
# створює в базі даних усі зареєстровані таблиці
