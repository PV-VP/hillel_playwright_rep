
from playwright.sync_api import Page, expect

def test_add_carr(authenticated_page) -> None:  # з authenticated_page
    authenticated_page.get_by_role("button", name="Add car").click()
    authenticated_page.get_by_label("Brand").select_option("1: 2")
    authenticated_page.get_by_label("Model").select_option("7: 8")
    authenticated_page.get_by_role("spinbutton", name="Mileage").click()
    authenticated_page.get_by_role("spinbutton", name="Mileage").fill("10")
    authenticated_page.get_by_role("button", name="Add").click()

    expect(authenticated_page.get_by_role("listitem").filter(has_text="BMW X5").last).to_be_visible()
    expect(authenticated_page.get_by_text("Car added")).to_be_visible()

def test_add_carr_2(auth_login) -> None:    #з auth_login -швидше
    auth_login.get_by_role("button", name="Add car").click()
    auth_login.get_by_label("Brand").select_option("1: 2")
    auth_login.get_by_label("Model").select_option("7: 8")
    auth_login.get_by_role("spinbutton", name="Mileage").click()
    auth_login.get_by_role("spinbutton", name="Mileage").fill("10")
    auth_login.get_by_role("button", name="Add").click()

    expect(auth_login.get_by_role("listitem").filter(has_text="BMW X5").last).to_be_visible()
    expect(auth_login.get_by_text("Car added")).to_be_visible()

def test_update_mileage(authenticated_page: Page) -> None:
    row = authenticated_page.get_by_role("listitem").first

    current_mileage = int(row.get_by_role("spinbutton").input_value())
    new_mileage = str(current_mileage + 1)

    row.get_by_role("spinbutton").fill(new_mileage)
    row.get_by_role("button", name="Update").click()

    expect(row.get_by_role("spinbutton")).to_have_value(new_mileage)
    expect(authenticated_page.get_by_text("Mileage updated")).to_be_visible()

def test_delete_car(authenticated_page: Page) -> None:
    authenticated_page.get_by_role("button").nth(2).click()
    authenticated_page.get_by_role("button", name="Remove car").click()
    authenticated_page.get_by_role("button", name="Remove").click()

    expect(authenticated_page.get_by_text("Car removed")).to_be_visible()