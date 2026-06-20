
# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    """функція вертає список з моженнями"""
    # Initialize the appropriate variable
    multiplier = 1
    result = 0
    lst = []
    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            break
            # Enter the action to take if the result is greater than 25
        lst.append(f'{number}x{multiplier}={result}')

        # Increment the appropriate variable
        multiplier += 1
    return lst
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
    if type(one) not in (int, float) or type(two) not in (int, float):
        raise TypeError('Аргументи мають бути числами')
    else:
        result = one + two
        return result

sum_two_didgits(2, 6)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(list_digit):

    len_list = len(list_digit)
    if len_list == 0:
        raise ValueError('Список не повинен бути порожнім')
    res = 0

    for el in list_digit:
        if type(el) not in (int, float):
            raise TypeError ('В списку мають бути тільки числа')
        res += el
    return res/len_list

arithmetic_mean([2, 4, 5])

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def str_revert(word):
    if type(word) != str:
        raise TypeError ('Значення має бути рядком')
    return word[::-1]

str_revert('Привіт світ')

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
fruits = ["яблуко", "банан", "апельсин", "диня", "персик", "ківі", "груша", "слива", "манго"]

def longest_word(fruits):
    count = ''
    len_fuits = len(fruits)
    if len_fuits == 0:
        raise ValueError('Список не повинен бути порожнім')

    for el in fruits:
        if len(el) > len(count):
            count = el
    return count

longest_word(fruits)