import pytest   # бібліотека для тестування

from core.facad import ApiClient    # клас-фасад, що об'єднує всі API-клієнти (expense, car і т.д.) в один об'єкт
from tests.api_test.car_tests.expense_test import CAR_ID    # імпорт ID машини з тестового файлу, щоб не дублювати константу


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