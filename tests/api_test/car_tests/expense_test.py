
CAR_ID = 545393  # ID машини для тесту — константа, яку імпортують інші файли

def test_expenses_test(api):    # тест з ручним циклом створення/видалення, без спеціальної фікстури для teardown

    next_mileage = api.expense.get_next_mileage(CAR_ID)  # отримує валідний пробіг для нової витрати

    post_expenses = api.expense.post_expense({  # створює витрату
        "carId": CAR_ID,
        "reportedAt": "2026-08-03",
        "mileage": next_mileage,
        "liters": 15,
        "totalCost": 11,
        "forceMileage": False
    })
    expense_id = post_expenses.json().get('data').get('id')  # витягує ID з відповіді

    expense_id_to_delete = api.expense.delete_expense(post_expenses.json()["data"]["id"])   # видаляє щойно створену витрату (ID дістається повторно напряму з JSON)
    expense_resp_id = api.expense.get_expense_by_id(expense_id, 404)    # перевіряє, що витрата видалена (очікує 404)


def test_expense_by_id(create_and_delete_expense):  # тест, де створення і видалення робить фікстура
    api, response_create_expense = create_and_delete_expense    # отримує клієнт і відповідь від фікстури
    expense_id = response_create_expense.json().get('data').get('id')   # дістає ID створеної витрати
    expense_resp_id = api.expense.get_expense_by_id(expense_id)  # запитує цю витрату по ID
    assert expense_resp_id.json().get('data').get('id') == expense_id   # перевіряє, що сервер повернув саме той об'єкт (ID співпадають)