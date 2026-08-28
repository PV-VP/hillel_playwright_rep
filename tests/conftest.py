import pytest   # бібліотека для тестування
import os
import random

from dotenv import load_dotenv
from playwright.sync_api import Playwright, APIRequestContext, expect

from core.facad import ApiClient    # клас-фасад, що об'єднує всі API-клієнти (expense, car і т.д.) в один об'єкт
from tests.api_test.car_tests.expense_test import CAR_ID    # імпорт ID машини з тестового файлу, щоб не дублювати константу

load_dotenv()

@pytest.fixture(scope="session")    # фікстура створюється один раз на всю сесію тестів
def api_session() -> ApiClient:
    return ApiClient()  # створює єдиний екземпляр клієнта API

@pytest.fixture
def create_expense(api):     # залежить від фікстури api, pytest підставить її автоматично
    next_mileage = api.expense.get_next_mileage(CAR_ID)  # отримує коректний наступний пробіг, щоб уникнути конфлікту з попереднім
    post_expense_response = api.expense.post_expense({  # створює витрату  через
        "carId": CAR_ID,
        "reportedAt": "2026-08-03",
        "mileage": next_mileage,
        "liters": 15,
        "totalCost": 11,
        "forceMileage": False
    })
    return api, post_expense_response   # повертає клієнт і відповідь сервера для використання в тесті

@pytest.fixture
def delete_expense(api):
    list_obj_to_delete = [] # порожній список, куди тест сам додаватиме об'єкти для видалення
    yield api, list_obj_to_delete   # віддає керування тесту
    if list_obj_to_delete:  # якщо тест додав хоч один об'єкт у список
        for resp in list_obj_to_delete: # проходить по всіх доданих відповідях
            expense_id = resp.json().get('data').get('id')   # дістає ID витрати
            expense_id_to_delete = api.expense.delete_expense(expense_id)   # видаляє витрату
            expense_resp_id = api.expense.get_expense_by_id(expense_id, 404)    # перевіряє, що видалення відбулось (очікується 404)

@pytest.fixture
def create_and_delete_expense(create_expense):   # залежить від create_expense — спочатку відпрацює вона
    api, post_exense_response = create_expense  # розпаковує результат попередньої фікстури
    yield api, post_exense_response # віддає дані тесту
    expense_id = post_exense_response.json().get('data').get('id')  # дістає ID створеної витрати
    expense_id_to_delete = api.expense.delete_expense(expense_id)   # видаляє її
    expense_resp_id = api.expense.get_expense_by_id(expense_id, 404)    # перевіряє, що об'єкта більше немає (404)


@pytest.fixture(scope="session")
def api() -> ApiClient:
    return ApiClient()

@pytest.fixture()
def api_browser(playwright: Playwright):
    api_browser = playwright.request.new_context(
        base_url=os.getenv('BASIC_URL')
    )

    yield api_browser

    api_browser.dispose()

@pytest.fixture()
def api_pl(api_browser: APIRequestContext):
    response_login = api_browser.post(
        url='/api/auth/signin',
        data={
            "email": os.getenv('USER_LOGIN'),
            "password": os.getenv('USER_PASSWORD'),
        }
    )
    expect(response_login).to_be_ok()
    yield api_browser



@pytest.fixture
def delete_car_api(api):
    list_obj_to_delete = []
    yield list_obj_to_delete
    if list_obj_to_delete:
        for resp in list_obj_to_delete:
            car_id_to_delete = api.car.delete_car(resp)
            car_reps_id = api.car.get_car_by_id(resp, 404)


@pytest.fixture
def delete_car(api):
    list_obj_to_delete = []
    yield api, list_obj_to_delete
    if list_obj_to_delete:
        for resp in list_obj_to_delete:
            car_id = resp.json().get('data').get('id')
            car_id_to_delete = api.car.delete_car(car_id)
            car_reps_id = api.car.get_car_by_id(car_id, 404)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "base_url": os.getenv('BASIC_URL'),
        "http_credentials": {
            "username": os.getenv('BASIC_AUTH_USER'),
            "password": os.getenv('BASIC_AUTH_PASS')
        }
    }

@pytest.fixture
def our_first_fixture():
    str_to_test = f'ID USER {random.choice(range(1, 23454))}'

    yield str_to_test
    print(f'I DELETE USER {our_first_fixture}')

@pytest.fixture
def create_and_delete_user(our_first_fixture):
    print(f'I CREATE USER {our_first_fixture}')
    yield our_first_fixture
    print(f'I DELETE USER {our_first_fixture}')


@pytest.fixture
def create_and_delete_user_1():
    print(f'I CREATE USER')

@pytest.fixture
def create_user():
    value_to_return = 'I CREATE USER {random.choice(range(1, 23454))} _V2'
    print(value_to_return)
    yield our_first_fixture

@pytest.fixture(scope='function')
def delete_user():
    object_values = []
    yield object_values
    if object_values:
        for value in object_values:
            ids = value
            print(f'DELETE USER {ids}')

#

@pytest.fixture
def create_and_delete_user_v2(create_user, delete_user):
    create_user, delete_user = create_user, delete_user
    yield create_user, delete_user

@pytest.fixture
def create_car(api):
    post_car_response = api.car.post_car({"carBrandId": 1, "carModelId": 1, "mileage": 122})
    return api, post_car_response

@pytest.fixture
def create_and_delete_car(create_car):
    api, post_car_response = create_car
    yield api, post_car_response
    car_id = post_car_response.json().get('data').get('id')
    api.car.delete_car(car_id)
    api.car.get_car_by_id(car_id, 404)