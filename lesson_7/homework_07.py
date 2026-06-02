# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    result = 0
    # Complete the while loop condition.
    while result < 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result <= 25:
            # Enter the action to take if the result is greater than 25
            print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_didgits(one, two):
    result = one + two
    return result

sum_two_didgits(2, 6)
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(list_digit):
    res = 0
    len_list = len(list_digit)

    for el in list_digit:
        res += el
    return res/len_list

arithmetic_mean([2, 4, 5])
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def str_revert(word):
    return word[::-1]

str_revert('Привіт світ')
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
fruits = ["яблуко", "банан", "апельсин", "диня", "персик", "ківі", "груша", "слива", "манго"]

def longest_word(fruits):
    count = ''

    for el in fruits:
        if len(el) > len(count):
            count = el
    return count

longest_word(fruits)
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()
"""
len_set = len({i for i in input()})
if len_set > 10:
    print('True')
else:
    print('False')
"""
def unique_symbols(text):

    len_set = len({i for i in text})

    if len_set > 10:
        print(True)
    else:
        print(False)


unique_symbols(input())


# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
#
"""
while 'h' not in input().lower():
    print('Ти в циклі. Для виходу натисни h або H')
"""
def find_h(text):

    while 'h' not in text.lower():
        print('Ти в циклі. Для виходу натисни h або H')
        text = input()

find_h(input())

# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Данні в лісті можуть бути будь якими
"""
res = [element for element in lst1 if type(element) == str]
print(res)
"""
def list_str(lst):
    lst_ = [element for element in lst if type(element) == str]
    return lst_

list_str(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])


#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
"""
res = sum([element for element in lst if element % 2 == 0])
print(res)
"""
def sum_all_even_numbers(lst_digits):
    return sum([el for el in lst_digits if el % 2 == 0])

sum_all_even_numbers([1, 21, 34, 22, 56, 87, 6, 23, 4])