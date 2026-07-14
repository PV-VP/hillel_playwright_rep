import logging
from datetime import datetime

file_path = 'hblog.txt'
key = 'TSTFEED0300|7E3E|0400'

logger = logging.getLogger('Heartbeat_Loger')           # Створюємо об'єкт логера
file_handler = logging.FileHandler('hb_test.log')       # Обробник, який пише логи в hb_test

logger.setLevel(logging.WARNING)                        # Мінімальний рівень логування WARNING
logger.addHandler(file_handler)                         # Щоб повідомлення записувались у файл

def make_file(document):                                # Функція читає файл та повертає список усіх строк з нього
    lst = []
    with open(document, 'r') as doc:                    # Відриваєм файл
        for i in doc:
            lst.append(i)
    return lst

def sort_by_key(logs):                                  # Функція відбирає тільки ті строки, які містять потрібний ключ
    lst2 = []
    for i in logs:
        if key in i:
            lst2.append(i)
    return lst2


def heartbeat_loger(filtered_logs):                         # Функція аналіз різниці між heartbeat та записує у лог
    prev_date = None                                        # пуста дата, потім туди потрапить попередня

    for i in filtered_logs:
        indx = i.find("Timestamp ")                         # Знаходимо індекс слова Timestamp у строці
        find_index = i[indx + 10 : indx + 18]               # Отримуєм строку дати
        date = datetime.strptime(find_index, "%H:%M:%S")  #Перетворюєм в час(об'єкт datetime)

        if prev_date is not None:   # якщо попередня дата не пуста
            dif = prev_date - date  # Рахуємо різницю між попереднім та поточним heartbeat
            seconds = dif.total_seconds()               # Переводимо різницю часу у секунди
            if 31 < seconds < 33:
                logger.warning(f"Heartbeat {seconds} sec. Time: {find_index}")
            elif seconds >= 33:
                logger.error(f"Heartbeat {seconds} sec. Time: {find_index}")
        prev_date = date                # Зберігаємо поточний час як попередній для наступної перевірки

logs = make_file(file_path)
res = sort_by_key(logs)
heartbeat_loger(res)



