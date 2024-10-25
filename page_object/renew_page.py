import allure
from page_object.base_page import BasePage
from locators.renew_locators import RenewLocators as RenLoc
from conftest import reference
from data import Data
from selenium.webdriver.common.by import By


class RenewPage(BasePage):

    @allure.title('Открыть урлом страницу "Восстановление пароля"')
    def open_forgot_password_page(self):
        self.open_page(f'{Data.URL}{Data.FORGOT_PASSWORD}')

    @allure.title('Лого')
    def title_check(self):
        return self.exist_check((By.XPATH, RenLoc.RENEW_PASSWORD_LOGO))

    @allure.title('Ввод данных в поле ввода "Email"')
    def input_email(self, reference):
        self.wait_and_text((By.XPATH, RenLoc.EMAIL), reference['email'])

    @allure.title('Наличия поля ввода "Пароль"')
    def exist_password_field_check(self):
        return self.exist_check((By.XPATH, RenLoc.NEW_PASSWORD))

    @allure.title('Ввод данных в поле "Пароль"')
    def input_password(self, reference):
        self.wait_and_text((By.XPATH, RenLoc.NEW_PASSWORD), reference['password'])

    @allure.title('Статуса подсветки границ поля "Пароль"')
    def stroke_password_field_check(self):
        if self.visibility_of_element(By.XPATH, RenLoc.ACTIVE_PASSWORD):
            return True

    @allure.title('Статуса поля ввода "Пароль"')
    def active_password_field_check(self):
        if self.visibility_of_element(By.XPATH, RenLoc.ACTIVE_PASSWORD):
            return True

    @allure.title('Прекод для "Показать/скрыть"')
    def precondition_for_show_hide_button(self, reference):
        self.open_forgot_password_page()
        self.input_email(reference)
        self.click_element_if_clickable((By.XPATH, RenLoc.RENEW_BUTTON))