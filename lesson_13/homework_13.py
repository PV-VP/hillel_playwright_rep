"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging



def log_event(username: str, status: str):

    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
    )
    logger = logging.getLogger("log_event")

    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    # logging.basicConfig(
    #     filename='login_system.log',
    #     level=logging.INFO,
    #     format='%(asctime)s - %(message)s'
    #     )
    # logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

"""нижче без юніттестів, самі тести в файлі test_login.py"""
def test_log_event():
    log_event('Pavlo', 'success')
    read_file = open('login_system.log')
    content = read_file.read()
    read_file.close()

    if 'Pavlo' in content and 'success' in content:
        print('OK: Pavlo/success знайдено в логах')
    else:
        print('FAIL: Pavlo/success не знайдено')

    log_event('Ivan', 'expired')
    read_file = open('login_system.log')
    content = read_file.read()
    read_file.close()

    if 'Ivan' in content and 'expired' in content:
        print('OK: Ivan/expired знайдено в логах')
    else:
        print('FAIL: Ivan/expired не знайдено')

    log_event('Egor', 'failed')
    read_file = open('login_system.log')
    content = read_file.read()
    read_file.close()

    if 'Egor' in content and 'failed' in content:
        print('OK: Egor/failed знайдено в логах')
    else:
        print('FAIL: Egor/failed не знайдено')


test_log_event()