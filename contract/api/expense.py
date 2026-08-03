from core.api_session import ApiSession


class ExpensesRequest(ApiSession):
    def __init__(self):
        super().__init__()
        self.path = '/api/expenses'

    def get_expense(self, params: dict = None, status_code: int = 200):
        # GET-запит на /api/expenses - отримує список витрат
        resp = self.get(path=self.path, params=params)
        assert resp.status_code == status_code, f'status code if not {status_code}'
        return resp

    def get_next_mileage(self, car_id: int):
        resp = self.get_expense(params={"carId": car_id})
        expenses_data = resp.json()['data']
        if not expenses_data:
            return 0
        return max(item['mileage'] for item in expenses_data) + 1

    def post_expense(self, payload: dict, status_code: int = 200):
        # POST-запит на /api/expenses - створює новий запис витрати
        resp = self.post(path=self.path, payload=payload)
        assert resp.status_code == status_code, f'status code if not {status_code}'
        return resp

    def delete_expense(self, item_id: int, status_code: int = 200):
        resp = self.delete(item_id=item_id)
        assert resp.status_code == status_code, f'status code if not {status_code}'
        return resp

    def get_expense_by_id(self, item_id: int, status_code: int = 200):
        resp = self.get(item_id=item_id)
        assert resp.status_code == status_code, f'status code if not {status_code}'
        return resp
