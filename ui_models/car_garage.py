from playwright.sync_api import Page

from ui_models.base_page import BasePage


class CarGaragePage(BasePage):
    PATH = '/panel/garage'

    def __init__(self, page: Page):
        super().__init__(page)
        self.button_add_car = page.locator('button[class="btn btn-primary"]')
        self.modal_title = page.locator('//div[@class="modal-content"]//h4')
        self.brand_drop_down = page.locator('#addCarBrand')
        self.brand_drop_down_value = page.locator('select[id="addCarBrand"] option')
        self.car_model_drop_down = page.locator('#addCarModel')
        self.car_mileage_input = page.locator('#addCarMileage')
        self.car_button_add_car = page.locator('[class="modal-footer d-flex justify-content-end"] button[class="btn btn-primary"]')