#Xpath
"""функція text()"""
sign_in = "//button[text()='Sign In']"
forgot_password_btn ="//button[text()='Forgot password']"
support_link = "//a[text()='support@ithillel.ua']"
contacts_link_display = "//a[text()='ithillel.ua']"
empty_car_message = "//p[text()='You don’t have any cars in your garage']"
garage_title = "//h1[text()='Garage']"
add_car_button = "//button[text()='Add car']"
add_car_expense = "//button[text()='Add an expense']"
profile_photo = "//img[@class='profile_photo' and @alt='User photo']"

"""по атрибуту"""
log_in_email = "//input[@name='email']"
instructions_button ="//a[@routerlink='instructions']"
model_select_dropdown = "//button[@id='modelSelectDropdown']"
add_car_mileage = "//input[@name='mileage']"
add_car_brand = "//select[@name='carBrandId']"
user_nav_dropdown = "//button[@id='userNavDropdown']"
edit_profile_button = "//button[@class='btn btn-primary']"
garage_link = "//a[@routerlink='/panel/garage']"

"""Складні локатори"""
log_in_pass = "//input[@name='password' and @type='password' and @id='signinPassword']"
profile = "//a[@routerlink='/panel/profile' and @routerlinkactive='disabled']"
instructions = "//a[@routerlink='/panel/instructions' and @class='btn header-link']"
select_car = "//select[@name='carModelId' and @id='addCarModel' and formcontrolname='model']"
input_milleage = "//input[@type='number' and @name='mileage' and @id='addCarMileage']"
garage_add_car_model = "//select[@name='carModelId' and @formcontrolname='model']"
car_select_dropdown = '//button[@id="modelSelectDropdown" and @aria-expanded="false"]'
fuel_expenses = '//a[@routerlink="/panel/expenses" and @routerlinkactive="disabled"]'

#css
"""
#        → пошук за id
.        → пошук за class
[]       → пошук за атрибутом
пробіл   → будь-який нащадок
>        → прямий дочірній елемент
+        → безпосередній наступний сусід
~        → наступні сусідні елементи
:first-child     → перший дочірній елемент
:last-child      → останній дочірній елемент
:nth-child(n)    → n-й дочірній елемент
:disabled        → вимкнений елемент
:enabled         → увімкнений елемент
:checked         → вибраний checkbox/radio
:not(...)        → елемент, який НЕ відповідає умові
"""
add_car_expense = 'button.btn.btn-primary:disabled'
instructions_search_button = 'button.instructions-search-controls_search'
brand_dropdown = "#brandSelectDropdown"
model_dropdown = "#modelSelectDropdown"
input_mileage = "input#addCarMileage"
input_mileage_by_attribute = 'input[name="mileage"]'
select_car = 'select[id="addCarModel"]'
log_out_button = 'button[ngbdropdownitem].user-nav_link'
fuel_expenses = 'a[routerlink="/panel/expenses"][href="/panel/expenses"]'
model_option = 'li[ngbdropdownitem].model-select-dropdown_item'

# Складні / дочірні
download_instruction = 'a.instruction-link_download[href*="Rear"][href*="audi/tt"]'
model_dropdown_enabled = 'button#modelSelectDropdown:enabled'
user_nav_dropdown = "button#userNavDropdown"
garage_link = 'p.h3.panel-empty_message > a[routerlink="/panel/garage"]'
edit_profile_button = 'button.btn.btn-primary[button]'
not_found_title = '.not-found_title'
add_car = 'div.panel-page_heading > button.btn.btn-primary'
icon_path = 'path[fill="#ECEEEF"]'
fuel_expenses_link = 'a.header-link[routerlink="/panel/expenses"]'
instructions_link = 'a.header-link[routerlink="/panel/instructions"]'
first_path = 'path[fill="#54D226"]'
model_option_q7 = 'select#addCarModel > option:nth-child(3)'
add_button = 'button[type="button"]:disabled'
cancel_button = 'button.btn.btn-secondary[type="button"]'
mileage_input = 'input#addCarMileage[type="number"]'
logo_path = 'svg > path:first-child'