from sqlalchemy.dialects.postgresql import json

from core.api_session import ApiSession
from models.base_pydantic import ListResponseModel, BaseResponseModel
from models.car_model.car_payload import CarPost
from models.car_model.car_response import CarResponse


class CarRequest:
    def __init__(self, api: ApiSession = None):
        self.api = api if api else ApiSession()
        self.path = '/api/cars'

    def get_car(self,params: dict = None, status_code : int = 200):
        resp = self.api.get(params=params, path=self.path)
        assert resp.status_code == status_code, f'status code is not {status_code}'

        return resp

    def get_car_py(self,params: dict = None, status_code : int = 200):
        resp = self.api.get(params=params, path=self.path)
        assert resp.status_code == status_code, f'status code is not {status_code}'

        return ListResponseModel[CarResponse].from_response(resp)

    def post_car(self, our_payload: dict, status_code: int = 201):
        resp = self.api.post(payload=our_payload, path=self.path)
        assert resp.status_code == status_code, f'status code is not {status_code}'
        return resp

    def post_car_py(self, our_payload: CarPost, status_code: int = 201):
        resp = self.api.post(payload=our_payload.to_dict(), path=self.path)
        assert resp.status_code == status_code, f'status code is not {status_code}'
        return BaseResponseModel[CarResponse].from_response(resp)


    def delete_car(self, item_id: dict, status_code : int = 200):
        resp = self.api.delete(path=f'{self.path}/{item_id}')
        assert resp.status_code == status_code, f'status code is not {status_code}'
        return resp

    def get_car_by_id(self, item_id: dict, status_code : int = 200):
        resp = self.api.get(path=f'{self.path}/{item_id}')
        assert resp.status_code == status_code, f'status code is not {status_code}'
        return resp