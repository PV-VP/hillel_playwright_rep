import logging  # для логування запитів/відповідей
import os   # для доступу до змінних середовища
from pathlib import Path    # для побудови шляхів незалежно від ОС

import requests # бібліотека HTTP-запитів
from dotenv import load_dotenv  # завантажує змінні з .env файлу

load_dotenv(Path(__file__).parent.parent / "utils" / ".env") #завантажує змінні з .env

logger_api = logging.getLogger('api')    # окремий логер з ім'ям 'api' для запису запитів/відповідей

class ApiSession:
    """Клас для налаштування та зберігання HTTP-сесії при роботі з API."""
    def __init__(self, token = None):
        self.user_login = os.getenv("USER_LOGIN")
        self.user_password = os.getenv("USER_PASSWORD")
        self.base_url = os.getenv("BASIC_URL")
        self.session = requests.Session()
        self.__token = token    # приватне поле для токена авторизації (sid)

    @property
    def token(self):
        if self.__token is None:
            self.get_token()
        return self.__token

    def get_token(self):
        resp = self.session.post(url=f'{self.base_url}/api/auth/signin',    # запит на логін з email/паролем
                                 json={"email":self.user_login,
                                       "password":self.user_password,
                                       "remember":False}
        )
        if resp.status_code != 200:
            raise AttributeError("Authentication failed")   # якщо логін не вдався — виняток
        token = resp.cookies.get('sid') # дістає токен сесії з cookie 'sid'
        if token is None:       # якщо токена немає — помилка
            raise AttributeError("Invalid token")

        self.__token = token    # зберігає токен у полі класу


    def auth(self):
        if self.__token is None: # якщо токена ще немає — логінитись і отримати
            self.get_token()
        else:
            self.session.cookies.update({'sid': self.__token})  # якщо токен вже є — просто підставити в cookies (без повторного логіну)

    def get(self, **kwargs):
        self.auth()  # гарантує, що сесія авторизована перед запитом
        if 'item_id' in kwargs:  # якщо переданий item_id — URL з ID в кінці (запит конкретного об'єкта)
            url_ = f'{self.base_url}{kwargs.get("path")}/{kwargs.get('item_id')}'
        else:
            url_ = f'{self.base_url}{kwargs.get("path")}'  # інакше — URL без ID (запит списку)
        logger_api.info(f'Request -> Method: GET for url:{url_}')  # логи для методу
        resp = self.session.get(url=f'{url_}', params=kwargs.get("params"))  # GET-запит з опційними query-параметрами
        logger_api.info(f'Response -> status code:{url_} resp:{resp.json()}')  # лог статусу і тіла відповіді
        return resp

    def post(self, **kwargs):
        self.auth()
        logger_api.info(f'Request -> Method: POST for url:{self.base_url}{kwargs.get("path")} Payload:{kwargs.get("payload")}')  #логи для методу
        resp = self.session.post(url=f'{self.base_url}{kwargs.get("path")}', json=kwargs.get("payload")) # POST-запит з JSON-тілом
        logger_api.info(f'Response -> status code:{resp.status_code} resp:{resp.json()}')
        return resp

    def delete(self, **kwargs):
        self.auth()
        logger_api.info(f'Request -> Method: DELETE for url:{self.base_url}{kwargs.get("path")}')  # логи для методу
        resp = self.session.delete(url=f'{self.base_url}{kwargs.get("path")}')  # DELETE-запит з ID об'єкта в URL
        logger_api.info(f'Response -> status code:{resp.status_code} resp:{resp.json()}')
        return resp


