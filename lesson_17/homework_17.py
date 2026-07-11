import logging

"""Генератори:
Напишіть генератор, який повертає послідовність парних чисел від 0 до N."""

def mi_generator(digit):

    for x in range(digit + 1):
        if x % 2 == 0:
            yield x

a = mi_generator(10)
for i in a:
    print(i)


print('-' * 50)
"""Створіть генератор, який генерує послідовність Фібоначчі до певного числа N."""

def generator_fib(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

fib = generator_fib(100)
for _ in fib:
    print(_)

print('-' * 50)
"""Ітератори:
Реалізуйте ітератор для зворотного виведення елементів списку.
"""

class Iterator:
    def __init__(self, lst):            # конструктор отримує список і створює початковий стан ітератора
        self.lst = lst                  # зберігаєм об'єкт ліст
        self.indx = len(lst) - 1        # запам'ятовуєм останній індекс, для початку перебору

    def __iter__(self):                 # метод повертає сам об'єкт, бо цей клас є ітератором
        return self                     # повертаємо поточний ітератор для перебору в циклі

    def __next__(self):
        if self.indx >= 0:              # перевірка чи є ще елементи в списку
            res = self.lst[self.indx]   # отримуємо елемент списку за поточним індексом
            self.indx -= 1              # відматуєм назад
            return res                  # повертаємо поточний елемент ітератора
        else:
            raise StopIteration


lst = Iterator([1, 2, 3, 4, 5])
for el in lst:
    print(el)
print('-' * 50)

"""Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N."""

class IteratorEvenNumbers():
    def __init__(self, max_num):
        self.max_num = max_num          #межа до якої йдемо
        self.current = 0                #число з якого починаєм

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.max_num:
            res = self.current
            self.current += 1

            if res % 2 == 0:
                return res
        raise StopIteration

d = IteratorEvenNumbers(10)
for el in d:
    print(el)


print('-' * 50)

"""Декоратори:
Напишіть декоратор, який логує аргументи та результати викликаної функції."""

logging.basicConfig(
    level=logging.INFO,                     # всі повідомлення рівня INFO і вище
    format="%(levelname)s - %(message)s"    # вигляд повідомлень у консолі
)

def log_arg_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Функція {func.__name__} визвана") # записуємо в лог назву функції
        logging.info(f'Arguments: {args}, {kwargs}')     # аргументи
        result = func(*args, **kwargs)
        logging.info(f'Result: {result}')
        return result
    return wrapper

@log_arg_decorator
def some_funk(one, two):
    return one + two

some_funk(10,20)

print('-' * 50)

"""Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції."""

def try_except_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except TypeError as error:
            logging.error(f'Помилка у функції {func.__name__}: {error}')
            raise error

    return wrapper

@try_except_decorator
def two_digits(one, two):
    return one + two
two_digits(1, 2)