import pytest

from models.car_model.car_payload import CarPost

@pytest.mark.api_test
def test_with_py(api):
    api.car.post_car({"carBrandId": 1, "carModelId": 1, "mileage": 122})
    resp = api.car.get_car_py()
    assert resp.status_code == 200
    assert resp.data[0].brand == "Audi"

@pytest.mark.api_test
def test_car_test(api):
    print(api.brand.base_url)
    response_car = api.car.get_car()
    post_car = api.car.post_car(our_payload={"carBrandId": 1,"carModelId": 1,"mileage": 122})
    car_id = post_car.json().get('data').get('id')
    car_id_to_delete = api.car.delete_car(car_id)
    car_reps_id = api.car.get_car_by_id(car_id, 404)
    # requests.post('https://qauto.forstudy.space/api/cars', json={'carBrandId': 1, 'carModelId': 1, 'mileage': 122}, cookies={'sid': "s%3AR_KNsnZ9UzornjRAFuUWLd-dfcW8BSjS.e6XGK5BGs1sB8C%2FOzXBMla78%2BchTA5LOF1v7KkV23Mw"})


@pytest.mark.api_test
def test_car_by_id(create_and_delete_car):
    api , response_create_car = create_and_delete_car
    car_id = response_create_car.json().get('data').get('id')
    car_reps_id = api.car.get_car_by_id(car_id)
    assert car_reps_id.json().get('data').get('id') == car_id

@pytest.mark.api_test
def test_delete_car(delete_car):
    api, list_obj_to_delete = delete_car
    post_car = api.car.post_car(our_payload={"carBrandId": 1,"carModelId": 1,"mileage": 122})
    post_car_1 = api.car.post_car(our_payload={"carBrandId": 1,"carModelId": 1,"mileage": 122})
    list_obj_to_delete += [post_car, post_car_1]

@pytest.mark.api_test
def test_delete_all_car(api):
    response_car = api.car.get_car()
    for car in response_car.json().get('data'):
        api.car.delete_car(item_id=int(car.get('id')))

@pytest.mark.api_test
def test_delete_all_car_pl(api_pl):
    response_car = api_pl.get('/api/cars')
    assert response_car.status == 200
    for car in response_car.json().get('data'):
        api_pl.delete(f'/api/cars/{car.get('id')}')
        response_get_by_id = api_pl.get(f'/api/cars/{car.get('id')}')
        assert response_get_by_id.status == 404
    response_car_after_delete = api_pl.get('/api/cars')
    assert len(response_car_after_delete.json().get('data')) == 0

