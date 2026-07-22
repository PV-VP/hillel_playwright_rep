    import psycopg2

    def connect_db():
        connection = psycopg2.connect(      # заходим у PostgreSQL.
            host="localhost",               # PostgreSQL локально
            port="5432",                    # стандартний порт
            user="postgres",
            password="1986",
            database="internet_shop"
        )
        print("Підключено")
        return connection

    connection = connect_db()
    cursor = connection.cursor()

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

    def create_table_categories(cursor):
    #categories table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories(  
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        );
        """)
    create_table_categories(cursor)

    def create_table_products(cursor):
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
    create_table_products(cursor)

    #заповнюєм categories
    def insert_categories(cursor):
        cursor.execute("""
        INSERT INTO categories (name)
        VALUES
        ('Телефони'),
        ('Ноутбуки'),
        ('Аксесуари');
        """)

    insert_categories(cursor)

    def insert_products(cursor):
    #заповнюєм products
        cursor.execute("""
        INSERT INTO products (name, description, price, category_id)
        VALUES
        ('iPhone 16', 'Новий смартфон Apple', 999.99, 1),
        ('Lenovo ThinkPad', 'Ноутбук для роботи', 1200.00, 2),
        ('Бездротова мишка', 'Комп''ютерний аксесуар', 25.50, 3);
        """)

    insert_products(cursor)

    connection.commit()     # Зберігаємо створення таблиць і додані дані в PostgreSQL

    def show_products(cursor):
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
        result = cursor.fetchall()  # забирає всі рядки, які повернув PostgreSQL
        return result

    result = show_products(cursor)


    for row in result:  #проходим по результату для друку
        print(row)

    cursor.close()      # закриваємо курсор
    connection.close()  #Закриваэм з'єднання