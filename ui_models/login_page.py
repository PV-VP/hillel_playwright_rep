from playwright.sync_api import Page

from ui_models.base_page import BasePage

# page.get_by_role("button", name="Sign In").click()
# page.locator('#signinEmail').fill("nedzelnytskyidev+hillel02026@gmail.com")
# page.get_by_role("textbox", name="Password").fill("AYf3JtDQnAcMbnc")
# expect(page.get_by_role("button", name="Login")).to_be_visible()
# expect(page.locator("app-signin-modal")).to_contain_text("Login")
# page.get_by_role("button", name="Login").click()
# page.wait_for_load_state("networkidle")
# expect(page.locator('//app-alert')).to_have_text('You have been successfully logged in')

class LoginPage(BasePage):
    PATH = '/panel/expenses'
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.button_signin = page.get_by_role("button", name="Sign In")
        self.email_edit_form = page.locator('#signinEmail')
        self.password_edit_form = page.get_by_role("textbox", name="Password")
        self.button_login_in_signin_form = page.get_by_role("button", name="Login")

    def login(self, email:str, password:str) -> None:
        self.button_signin.click()
        self.email_edit_form.fill(email)
        self.password_edit_form.fill(password)
        self.button_login_in_signin_form.click()

