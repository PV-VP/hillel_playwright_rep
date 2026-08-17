import os
from pathlib import Path

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect, Browser

from core.facad import ApiClient
from ui_models.base_page import BasePage

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent.parent.parent / "utils" / ".env")

@pytest.fixture(scope="session")    # фікстура створюється один раз на всю сесію тестів
def api() -> ApiClient:
    return ApiClient()  # створює єдиний екземпляр клієнта API

@pytest.fixture
def delete_car_api(api):
    list_obj_to_delete = []
    yield list_obj_to_delete
    if list_obj_to_delete:
        for resp in list_obj_to_delete:
            expense_id_to_delete = api.expense.delete_car(resp)
            expense_resp_id = api.expense.get_expense_by_id(resp, 404)

@pytest.fixture
def delete_car(api):
    list_obj_to_delete = []
    yield api, list_obj_to_delete
    if list_obj_to_delete:
        for resp in list_obj_to_delete:
            car_id = resp.json().get('data').get('id')
            expense_id_to_delete = api.expense.delete_car(car_id)
            expense_resp_id = api.expense.get_expense_by_id(car_id, 404)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'ignore_https_errors': True,
        "base_url": os.getenv("BASIC_URL"),
        "http_credentials": {
            "username": os.getenv("BASIC_AUTH_USER"),
            "password": os.getenv("BASIC_AUTH_PASS"),
        },
    }


@pytest.fixture
def login_ui(page: Page) -> Page:
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
    expect(page.locator('//div[@class="alert alert-success"]')).to_have_text('You have been successfully logged in')
    yield page

@pytest.fixture
def auth_login(browser_context_args, browser: Browser, api_session: ApiClient) -> Page:
    token_api = api_session.api.token
    context = browser.new_context(
        **browser_context_args,
        storage_state={
            'cookies': [
                {
                    'name': 'sid',
                    'value': token_api,
                    'domain': '.forstudy.space',
                    'path': '/',
                }
            ]
        }
    )
    page  = context.new_page()
    base_page = BasePage(page)
    base_page.open()
    expect(base_page.alert_danger_locator).not_to_be_visible()
    yield page

    page.close()
    context.close()