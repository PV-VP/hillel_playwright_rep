import pytest
import requests  # Імпортуємо бібліотеку requests для виконання HTTP-запитів.
from requests.auth import HTTPBasicAuth  # Імпортуємо клас для авторизації через HTTP Basic Auth.

@pytest.fixture(scope='class')  # фікстура, яка буде виконана один раз для всього класу тестів.
def api_session():
    session = requests.Session()    # HTTP-сесія, яка буде використовуватись для всіх запитів

    resp = session.post(    # Виконуємо POST-запит на ендпоінт авторизації.
        "http://127.0.0.1:8080/auth",   # URL ендпоінта для отримання токена.
        auth=HTTPBasicAuth("test_user", "test_pass")    # Передаємо логін і пароль через HTTP Basic Authentication.
    )

    if resp.status_code != 200:
        raise AttributeError("Authentication failed")  # Якщо авторизація не пройшла — зупиняємо виконання тестів з помилкою

    token = resp.json().get('access_token')  # дістає токен сесії

    if token is None:  # перевірка що повернувся токен, а не Ноне(наприклад)
        raise AttributeError("Invalid token")

    session.headers.update({        # Додаємо JWT токен у заголовки сесії.
        "Authorization": f"Bearer {token}"})

    return session      # Повертаємо готову авторизовану сесію у тест.