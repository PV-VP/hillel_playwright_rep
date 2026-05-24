# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

people_records.insert(0,('Pasha', 'Mazurov', 39, 'QA Engineer', 'Kyiv')) #Додайте свій новий запис на початок даного списку.
print(people_records)
people_records[1], people_records[5] = people_records[5], people_records[1]#У модифікованому списку обміняйте елементи з індексами 1 і 5 (1<->5). Виведіть результат.
print(people_records)

age_6 = people_records[6][2]
age_10 = people_records[10][2]
age_13 = people_records[13][2]

if age_6 >= 30 and age_10 >= 30 and age_13 >= 30:
    print('Усі люди з індексами 6, 10, 13 мають вік ≥ 30')
else:
    if age_6 < 30:
        print(f"Має вік < 30: {people_records[6][0]} {people_records[6][1]}, вік {age_6}")
    if age_10 < 30:
        print(f"Має вік < 30: {people_records[10][0]} {people_records[10][1]}, вік {age_10}")
    if age_13 < 30:
        print(f"Має вік < 30: {people_records[13][0]} {people_records[13][1]}, вік {age_13}")


