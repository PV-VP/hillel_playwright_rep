from core.api_session import ApiSession


class UserRequest:
    def __init__(self, api: ApiSession = None):
        self.api = api if api else ApiSession()