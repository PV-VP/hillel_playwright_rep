# Створіть клас "Студент" з атрибутами "ім'я",
# "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент",
# який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.


class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score
    def info_student(self):
        print(f'Ім\'я студента: {self.name} \nФамілія студента: {self.surname} \nВік студента: {self.age}\nСередній бал:{self.average_score}')
    def change_average_score(self, new_average_score):
        self.average_score = new_average_score
        print('_' * 10)

student_1 = Student('Павло', 'Мазуров', 39, 4)
student_1.info_student()
student_1.change_average_score(5)
student_1.info_student()