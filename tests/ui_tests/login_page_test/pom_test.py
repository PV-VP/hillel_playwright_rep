import json
import os
import time

import pytest
from playwright.sync_api import Page, expect

from ui_models.car_garage import CarGaragePage
from ui_models.login_page import LoginPage

@pytest.mark.ui_test
def test_login_no_pom(page: Page) -> None:
    page.goto("/")
    # page2 = page.context.new_page()
    # page2.goto("https://seleniumbase.io/w3schools/iframes")
    page.get_by_role("button", name="Sign In").click()
    page.locator('#signinEmail').fill("nedzelnytskyidev+hillel02026@gmail.com")
    page.get_by_role("textbox", name="Password").fill("AYf3JtDQnAcMbnc")
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page.locator("app-signin-modal")).to_contain_text("Login")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")
    expect(page.locator('//app-alert')).to_have_text('You have been successfully logged in')

@pytest.mark.ui_test
@pytest.mark.parametrize('email, password, status', [
    (os.getenv('USER_LOGIN'),os.getenv('USER_PASSWORD'), 'success'),
    ('qwe@gmail.com', os.getenv('USER_LOGIN'), 'failed')])
def test_2(page:Page, email, password, status) -> None:
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(email,password)
    if status == 'success':
        expect(login_page.alert_success_locator).to_have_text('You have been successfully logged in')
    elif status == 'failed':
        expect(login_page.alert_danger_locator).to_have_text('Wrong email or password')

@pytest.mark.ui_test
def test_create_car(auth_login, delete_car_api):
    car_page = CarGaragePage(auth_login)
    car_page.open()
    car_page.button_add_car.click()
    expect(car_page.modal_title).to_have_text('Add a car')
    expect(car_page.brand_drop_down.locator("option")).to_have_text(['Audi', 'BMW', 'Ford', 'Porsche', 'Fiat'])
    car_page.brand_drop_down.select_option('Ford')  #підставить форд
    car_page.car_model_drop_down.select_option('Fusion')
    car_page.car_mileage_input.fill('123')
    with auth_login.expect_response('**/api/cars') as response_info:
        car_page.car_button_add_car.click()
        print(response_info)
    resp_car_id = response_info.value.json()['data']['id']
    delete_car_api.append(resp_car_id)
    expect(car_page.alert_success_locator).to_have_text('Car added')
