import logging
import pytest

logger = logging.getLogger(__name__)    # Створюємо логер для цього файлу.

@pytest.mark.parametrize(   # parametrize запускає один і той самий тест декілька разів
    "sort_by,limit",
    [
        ("price", 5),
        ("year", 10),
        ("brand", 10),
        ("engine_volume", 7),
        ("price", 15),
        ("year", 20)
    ]
)
def test_get_cars(api_session, sort_by, limit): # api_session — fixture, яка вже робить авторизацію, sort_by і limit — значення, які pytest підставляє із parametrize

    logger.info(f"Відправляємо GET /cars з параметрами sort_by={sort_by}, limit={limit}")       # Записуємо в лог інформацію:

    resp = api_session.get(    # Виконуємо GET-запит до endpoint /cars, params автоматично сформує query string: sort_by=price&limit=5
        'http://127.0.0.1:8080/cars',
        params={
            "sort_by": sort_by,
            "limit": limit
        }
    )

    logger.info(f"Отримали статус відповіді: {resp.status_code}")
    assert resp.status_code == 200      # Перевіряємо, що API повернув успішну відповідь.

    data = resp.json()      # Перетворюємо JSON-відповідь сервера у Python-об'єкт.
    logger.info(f"Отримали {len(data)} автомобілів")
    assert len(data) == limit       # Перевіряємо, що параметр limit працює.

    for car in data:        # Проходимо по кожному автомобілю дя перевірки типів
        assert isinstance(car['brand'], str)
        assert isinstance(car['year'], int)
        assert isinstance(car['engine_volume'], (int, float))
        assert isinstance(car['price'], (int, float))
    logger.info("Перевірка типів даних пройшла успішно")

    values = [car[sort_by] for car in data]     # Створюємо список значень поля, по якому сортуємо. Якщо sort_by = "price": буде:[28000, 29000, 30000, 32000]
    logger.info(f"Отримані значення для сортування: {values}")
    assert values == sorted(values)     # Перевіряємо, що значення відсортован. Якщо порядок неправильний — тест впаде.
    logger.info(f"Сортування по {sort_by} перевірено успішно")
    #print(resp.json())