import unittest
from homework_12 import multiplication_table, sum_two_didgits, arithmetic_mean, str_revert, longest_word, fruits

class TestFunctions(unittest.TestCase):

    def test_multiplication_table_outputs_correct_values(self):
        """перевірка границі не більше 25 для multiplication_table"""
        multiplication_table_values = multiplication_table(3)
        res = multiplication_table_values[-1].split('=') #берем останій елемент списка і розділяєм по "="
        self.assertLessEqual(int(res[-1]),25 )        #перевіряєм щоб результат  був не більше 25

    def test_check_list(self):
        """перевірка возврату всього списку при умові передачі в функцію 3 для multiplication_table"""
        multiplication_table_values = multiplication_table(3)
        self.assertEqual(multiplication_table_values, ['3x1=3',
                                                       '3x2=6',
                                                       '3x3=9',
                                                       '3x4=12',
                                                       '3x5=15',
                                                       '3x6=18',
                                                       '3x7=21',
                                                       '3x8=24'])

    def test_type_two_didgits_str(self):
        """Перевірка, що функція піднімає TypeError при передачі рядків для sum_two_didgits"""
        with self.assertRaises(TypeError):
            sum_two_didgits('1', '5')

    def test_sum_two_didgits_positive_numbers(self):
        """Перевірка арифметики додатних значень для sum_two_didgits"""
        sum_two_didgits_value = sum_two_didgits(2, 6)
        self.assertEqual(sum_two_didgits_value, 8)

    def test_arithmetic_negative_numbers(self):
        """Перевірка арифметики негативних значень для sum_two_didgits"""
        sum_two_didgits_negative = sum_two_didgits(-1, -3)
        self.assertEqual(sum_two_didgits_negative, -4)

    def test_arithmetic_mean_list(self):
        """Список не має бути порожнім для arithmetic_mean"""
        with self.assertRaises(ValueError):
            arithmetic_mean([])

    def test_arithmetic_mean_correctness(self):
        """Перевірка коректного обчислення середнього арифметичного для arithmetic_mean"""
        arithmetic_mean_value = arithmetic_mean([2, 4, 5])
        self.assertEqual(arithmetic_mean_value, 11 / 3)

    def test_arithmetic_mean_list_digit(self):
        """Перевірка елементів списку на тип число для arithmetic_mean"""
        with self.assertRaises(TypeError):
            arithmetic_mean(['1', 'asd', '@asd'])

    def test_str_revert_correctness(self):
        """Перевірка корректності вихідного значення для str_revert"""
        str_revert_values = str_revert('Привіт світ')
        self.assertEqual(str_revert_values, 'тівс тівирП')

    def test_str_revert_type_str(self):
        """Аргументи мають бути рядком для str_revert"""
        with self.assertRaises(TypeError):
            str_revert(1)

    def test_longest_word_list(self):
        """Список не має бути порожнім для longest_word"""
        with self.assertRaises(ValueError):
            longest_word([])

    def test_longest_word(self):
        """Перевірка що вертається найдовше слово зі списку для longest_word"""
        longest_word_value = longest_word(fruits)
        self.assertEqual(longest_word_value, "апельсин")

if __name__ == '__main__':
    unittest.main()