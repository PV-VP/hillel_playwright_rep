from contract.api.expense import ExpensesRequest
from core.api_session import ApiSession


class ApiClient:
    def __init__(self, token = None):
        self.api = ApiSession(token=token)
        self.expense = ExpensesRequest()
