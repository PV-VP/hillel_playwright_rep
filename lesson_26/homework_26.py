import os
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def authenticated_page(page: Page) -> Page:
    page.goto("/")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("textbox", name="Email").fill(os.getenv("USER_LOGIN"))
    page.get_by_role("textbox", name="Password").fill(os.getenv("USER_PASSWORD"))
    page.get_by_role("button", name="Login").click()
    expect(page.locator('//div[@class="alert alert-success"]/p')).to_have_text('You have been successfully logged in')
    return page


def test_add_carr(authenticated_page: Page) -> None:
    authenticated_page.get_by_role("button", name="Add car").click()
    authenticated_page.get_by_label("Brand").select_option("1: 2")
    authenticated_page.get_by_label("Model").select_option("7: 8")
    authenticated_page.get_by_role("spinbutton", name="Mileage").click()
    authenticated_page.get_by_role("spinbutton", name="Mileage").fill("10")
    authenticated_page.get_by_role("button", name="Add").click()

    expect(authenticated_page.get_by_role("listitem").filter(has_text="BMW X5").last).to_be_visible()


def test_update_mileage_bmw(authenticated_page: Page) -> None:
    row = authenticated_page.get_by_role("listitem").filter(has_text="BMW X5").last
    current_mileage = int(row.get_by_role("spinbutton").input_value())
    new_mileage = str(current_mileage + 1)

    row.get_by_role("spinbutton").click()
    row.get_by_role("spinbutton").fill(new_mileage)
    row.get_by_role("button", name="Update").click()

    expect(row.get_by_role("spinbutton")).to_have_value(new_mileage)


def test_update_mileage_porsche(authenticated_page: Page) -> None:
    row = authenticated_page.get_by_role("listitem").filter(has_text="Porsche Cayenne").last
    current_mileage = int(row.get_by_role("spinbutton").input_value())
    new_mileage = str(current_mileage + 1)

    row.get_by_role("spinbutton").click()
    row.get_by_role("spinbutton").fill(new_mileage)
    row.get_by_role("button", name="Update").click()

    expect(row.get_by_role("spinbutton")).to_have_value(new_mileage)


def test_delete_car(authenticated_page: Page) -> None:
    row = authenticated_page.get_by_role("listitem").filter(has_text="BMW X5").last
    row.get_by_role("button").last.click()
    authenticated_page.get_by_role("button", name="Remove car").click()
    authenticated_page.get_by_role("button", name="Remove").click()

    expect(authenticated_page.get_by_role("listitem").filter(has_text="BMW X5")).to_have_count(0)