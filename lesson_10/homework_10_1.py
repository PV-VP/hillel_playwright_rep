"""Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур,
та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур,
та у циклі порахуйте та виведіть в консоль площу та периметр кожної."""

from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def get_area(self):
        return self.__a * self.__b

    def get_perimeter(self):
        return 2 * (self.__a + self.__b)

class Square(Figure):
    def __init__(self, a):
        self.__a = a

    def get_area(self):
        return self.__a ** 2

    def get_perimeter(self):
        return 4 * self.__a

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_area(self):
        p = (self.__a + self.__b + self.__c) / 2
        return (p * (p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5

    def get_perimeter(self):
        return self.__a + self.__b + self.__c


figures = [Rectangle(5, 7),
           Square(4),
           Triangle(3, 3, 3)
           ]
for f in figures:
    print(f'Площа:{f.get_area()} \nПериметр:{f.get_perimeter()}')