# Створює Docker image (образ) для нашого застосунку

# Використовуємо офіційний образ Python версії 3.9
FROM python:3.12

# Задаємо робочу директорію контейнера
WORKDIR /app

#копіюєм наш файл в докер в папку /app
COPY requirements.txt .
# Встановлюємо залежності для тестування
RUN pip install -r requirements.txt

# Копіюємо файли з локальної директорії в контейнер
COPY . .

# Виконуємо команду для запуску тестів під час створення контейнера
CMD ["sh", "-c", "python -m contract.db.create_tables && python -m lesson_21.seed_data && pytest -m 'add or info or update or delete'"]