"""Завдання 1
Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
 які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department,
а клас Developer - атрибут programming_language.
Тепер створіть клас TeamLead, який успадковується як від Manager,
так і від Developer. Цей клас представляє керівника з команди розробників.
Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ),
а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead"""

class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, department,**kwargs):
        super().__init__(**kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, team_size, **kwargs):
        self.team_size = team_size
        super().__init__(**kwargs)

lead = TeamLead(
    team_size=5,
    department='Development',
    programming_language='Python',
    name='Ivan',
    salary=1000
)
print(lead.__dict__)
