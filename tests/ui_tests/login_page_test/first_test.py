import time

import pytest
from playwright.sync_api import Page, expect





def test_example_2(auth_login) -> None:
    page = auth_login
    page.goto("/")
    # # page2 = page.context.new_page()
    # # page2.goto("https://seleniumbase.io/w3schools/iframes")
    # page.get_by_role("button", name="Sign In").click()
    # page.locator('#signinEmail').fill("nedzelnytskyidev+hillel02026@gmail.com")
    # page.get_by_role("textbox", name="Password").fill("AYf3JtDQnAcMbnc")
    # expect(page.get_by_role("button", name="Login")).to_be_visible()
    # expect(page.locator("app-signin-modal")).to_contain_text("Login")
    # page.get_by_role("button", name="Login").click()
    # page.wait_for_load_state("networkidle")
    # expect(page.locator('//app-alert')).to_have_text('You have been successfully logged in')
    # expect(page.locator('//div[@class="alert alert-success"]')).to_have_text('You have been successfully logged in')



def test_exp_3(page: Page) -> None:
    page.goto("/")



def test_example(login_ui) -> None:
    page = login_ui
    page.goto("/")
    # # page2 = page.context.new_page()
    # # page2.goto("https://seleniumbase.io/w3schools/iframes")
    # page.get_by_role("button", name="Sign In").click()
    # page.locator('#signinEmail').fill("nedzelnytskyidev+hillel02026@gmail.com")
    # page.get_by_role("textbox", name="Password").fill("AYf3JtDQnAcMbnc")
    # expect(page.get_by_role("button", name="Login")).to_be_visible()
    # expect(page.locator("app-signin-modal")).to_contain_text("Login")
    # page.get_by_role("button", name="Login").click()
    # page.wait_for_load_state("networkidle")
    # expect(page.locator('//app-alert')).to_have_text('You have been successfully logged in')
    # expect(page.locator('//div[@class="alert alert-success"]')).to_have_text('You have been successfully logged in')

    time.sleep(5)

def test_hyper_link(page: Page) -> None:
    page.goto("/")
    # Get page after a specific action (e.g. clicking a link)
    with page.context.expect_page() as new_page_info:
        page.locator('//a[@href="https://ithillel.ua"]').click()  # Opens a new tab
    new_page = new_page_info.value

    # Interact with the new page normally
    assert new_page.title() == "Комп'ютерна школа Hillel Online: Курси IT-технологій"
    # expect(new_page.title()).to_have_title("Комп'ютерна школа Hillel Online: Курси IT-технологій", )
    # new_page.get_by_role("button").click()
    # print(new_page.title())



def test_checkbox(page: Page):
    page.goto("https://faculty.washington.edu/chudler/java/boxes.html")
    all_checkbox =  page.locator('input[type="checkbox"]').all()
    for checkbox in all_checkbox:
        checkbox.check()
    for index, checkbox_uncheck in enumerate(all_checkbox):
        if index % 2 == 0:
            checkbox_uncheck.uncheck()
            expect(checkbox_uncheck).not_to_be_checked()
        else:
            expect(checkbox_uncheck).to_be_checked()



def test_iframe(page: Page):
    page.goto('https://seleniumbase.io/w3schools/iframes')
    iframe_obj = page.frame_locator('#iframeResult')
    locator_p = iframe_obj.locator('//body/p')
    print(page.locator('#runbtn').inner_text())
    # assert locator_p.inner_text() == '123123'
    expect(locator_p).to_have_text('123123Use CSS width & height to specify the iframe size:')
    print(locator_p.inner_text())


def dialog_click(dialog, type_click=True):
    print(dialog.message)
    if type_click:
        dialog.accept()
    else:
        dialog.dissmiss()


def test_dilog_wind(page: Page):
        page.goto('https://testpages.eviltester.com/pages/basics/alerts-javascript/')
        page.on("dialog", lambda dialog: dialog_click(dialog=dialog))
        page.locator('#alertexamples').click()
        expect(page.locator('#alertexplanation')).to_have_text('You triggered and handled the alert dialog')
        page.on("dialog", lambda dialog: dialog_click(dialog=dialog))
        page.locator('#confirmexample').click()
        expect(page.locator('#confirmreturn')).to_have_text('true')
        page.reload()
        page.on("dialog", lambda dialog: dialog.dissmiss())
        page.locator('#confirmexample').click()
        expect(page.locator('#confirmreturn')).to_have_text('false')