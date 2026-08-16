import os

import pytest
from playwright.sync_api import Page, expect

from ui_models.login_page import LoginPage


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

@pytest.mark.parametrize('email, password',[(os.getenv('USER_LOGIN'),os.getenv('USER_PASSWORD')),])
def test_2(page:Page, email, password) -> None:
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(email,password)
    expect(login_page.alert_success_locator).to_have_text('You have been successfully logged in')
