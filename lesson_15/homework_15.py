import csv
import json
import logging
from pathlib import Path
import xml.etree.ElementTree as ET

"""Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх. 
Результат запишіть у файл result_<your_second_name>.csv"""

set_data = set()
header = None

with open(r"C:\Users\pasha\PycharmProjects\ithillel_playwright\lesson_15\csv_files\random.csv", 'r') as file1:
    reader_random = csv.reader(file1)
    header = next(reader_random)  # перший рядок — заголовок
    for row in reader_random:
        set_data.add(tuple(row))

with open(r"csv_files/random-michaels.csv", 'r') as file2:
    reader_random_michaels = csv.reader(file2)
    next(reader_random_michaels)  # пропускаємо заголовок другого файлу
    for row in reader_random_michaels:
        set_data.add(tuple(row))

with open('result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(set_data)


    """Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
     результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log"""

logger = logging.getLogger('JsonLog')                       # створюємо логер з ім'ям "JsonLog"
#logger.setLevel(logging.ERROR)                             # встановлюємо мінімальний рівень повідомлень, які буде обробляти логер
file_handler = logging.FileHandler('json_result.log')       # створюємо обробник (FileHandler), який записуватиме логи у файл json_result.log
file_handler.setLevel(logging.ERROR)                        # встановлюємо для обробника рівень ERROR
logger.addHandler(file_handler)                             # підключаємо обробник до логера, щоб логер записував повідомлення у файл

parent_dir = Path(r'C:\Users\pasha\PycharmProjects\ithillel_playwright\lesson_15\json_files')       # вказуєм шлях до папки з файлами по який ітеруємось
files = [f for f in parent_dir.iterdir() if f.is_file()]                                            # формуємо список усіх файлів, що знаходяться у цій папці

for file in files:                                              #ітруємось по файлам

    with open(file, 'r', encoding="utf-8") as json_file:        #відкриваємо поточний файл у режимі читання з кодуванням utf-8
        try:
            data = json.load(json_file)                         #пробуємо прочитати та перетворити вміст файлу у Python-об'єкт
            print(data)
        except json.JSONDecodeError as er:
            logger.error(f"Invalid JSON in file {file}: {er}")  #якщо ДЖсон невалідний, записуємо інформацію про помилку у лог-файл



"""Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення 
значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо"""

logger = logging.getLogger('XmlLog')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('xml_result.log')
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

# Завантаження XML-файлу
tree = ET.parse(r'C:\Users\pasha\PycharmProjects\ithillel_playwright\lesson_15\xml_files\groups.xml')
root = tree.getroot() # отримуємо кореневий елемент groups
# Пошук елементу

def find_value(root, number):

    for group in root.findall('group'):     # перебираємо всі елементи <group>
        group_number = group.find('number') # дістаємо тег <number> всередині group

        if group_number is not None and group_number.text == str(number): # перевіряємо чи номер співпадає з шуканим
            timing_exbytes = group.find('timingExbytes')

            incoming = timing_exbytes.find('incoming') # шукаємо тег incoming

            return incoming.text
    return None

result = find_value(root, 2)
logger.info(result)