import psycopg2

connection = psycopg2.connect(      # заходим у PostgreSQL.
    host="localhost",               # PostgreSQL локально
    port="5432",                    # стандартний порт
    user="postgres",
    password="1986",
    database="internet_shop"
)
print("Підключено")


#connection.autocommit = True        #автосейф
#cursor = connection.cursor()        #створює об'єкт, через який ми відправляємо SQL
#нова база
#cursor.execute("""
#CREATE DATABASE internet_shop
#""")
#print("База створена")
#cursor.close()
#connection.close()

#connection.autocommit = True        #автосейф
cursor = connection.cursor()        #об'єкт, через який відправляється SQL-команда у відкрите підключення

#categories table
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories(  
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
""")

#products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    price NUMERIC(10,2),
    category_id INTEGER REFERENCES categories(id)
);
""")
# category_id — зовнішній ключ, який посилається на id у таблиці categories

#заповнюєм categories
cursor.execute("""
INSERT INTO categories (name)
VALUES
('Телефони'),
('Ноутбуки'),
('Аксесуари');
""")

#заповнюєм products
cursor.execute("""
INSERT INTO products (name, description, price, category_id)
VALUES
('iPhone 16', 'Новий смартфон Apple', 999.99, 1),
('Lenovo ThinkPad', 'Ноутбук для роботи', 1200.00, 2),
('Бездротова мишка', 'Комп''ютерний аксесуар', 25.50, 3);
""")
connection.commit()     # Зберігаємо створення таблиць і додані дані в PostgreSQL

# JOIN-запит
cursor.execute("""
SELECT 
    products.name,
    products.description,
    products.price,
    categories.name AS category
FROM products
JOIN categories
ON products.category_id = categories.id;
""")

result = cursor.fetchall()  #забирає всі рядки, які повернув PostgreSQL

for row in result:  #проходим по результату для друку
    print(row)

cursor.close()      # закриваємо курсор
connection.close()  #Закриваэм з'єднання