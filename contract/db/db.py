import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних
#DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:1986@postgres-db:5432/students_db")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:1986@localhost:5432/students_db")
engine = create_engine(DATABASE_URL)
Base = declarative_base()   #клас до якого ми наслудіємся, має лежати коремо

# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()