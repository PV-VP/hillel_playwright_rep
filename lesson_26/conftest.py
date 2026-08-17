import os
from pathlib import Path

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect, Browser

from core.facad import ApiClient


load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent.parent / "utils" / ".env")

@pytest.fixture(scope="session")    # фікстура створюється один раз на всю сесію тестів
def api_session() -> ApiClient:
    return ApiClient()  # створює єдиний екземпляр клієнта API

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
def authenticated_page(page: Page) -> Page:
    page.goto("/")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("textbox", name="Email").fill(os.getenv("USER_LOGIN"))
    page.get_by_role("textbox", name="Password").fill(os.getenv("USER_PASSWORD"))
    page.get_by_role("button", name="Login").click()
    expect(page.locator('//div[@class="alert alert-success"]/p')).to_have_text('You have been successfully logged in')
    yield page

@pytest.fixture     #фикстура для автологина(щоб не вводити данні при вході, отримуєм токен)
def auth_login(browser_context_args, browser: Browser, api_session) -> Page:
    token_api = api_session.api.token
    context = browser.new_context(
        **browser_context_args,
        storage_state={
            'cookies': [
                {
                    'name': 'sid',
                    'value': token_api,
                    'domain': '.forstudy.space',
                    'path': '/'
                }
            ]
        }
    )
    page = context.new_page()
    page.goto("/")
    yield page

    page.close()
    context.close()