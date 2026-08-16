from playwright.sync_api import Page


class BasePage:
    PATH = '/'

    def __init__(self, page: Page):
        self.page = page
        self.alert_danger_locator = page.locator('div[class="alert alert-danger"]')
        self.alert_success_locator = page.locator('div[class="alert alert-success"]')

    def open(self):
        return self.page.goto(self.PATH)