import allure
from page_object.base_page import BasePage
from locators.renew_locators import RenewLocators as RenLoc
from conftest import reference
from data import Data


class RenewPage(BasePage):

    @allure.title('Лого')
    def logo_check(self):
        return self.exist_check(RenLoc.RENEW_PASSWORD_LOGO)

    @allure.title('Открыть урлом страницу "Восстановление пароля"')
    def open_forgot_password(self):
        self.open_page(f'{Data.URL}{Data.FORGOT_PASSWORD}')

    @allure.title('ввод данных в поле "Email"')
    def write_email(self, reference):
        self.wait_and_text(RenLoc.EMAIL, reference['email'])

    @allure.title('ввести данные в поле "Пароль"')
    def write_password(self, reference):
        self.wait_and_text(RenLoc.NEW_PASSWORD, reference['password'])

    @allure.title('статус подсветки поля "Пароль"')
    def status_circuit_password_field(self):
        if self.visibility_of_element(RenLoc.ACTUAL_PASSWORD):
            return True

    @allure.title('статус поля ввода "Пароль"')
    def status_password_field(self):
        if self.visibility_of_element(RenLoc.ACTUAL_PASSWORD):
            return True

    @allure.title('наличие поля ввода "Пароль"')
    def exist_password_field(self):
        return self.exist_check(RenLoc.NEW_PASSWORD)

    @allure.title('прекод для "Показать/скрыть"')
    def precondition_in_renew(self, reference):
        self.open_forgot_password()
        self.write_email(reference)
        self.click_element_if_clickable(RenLoc.RENEW_BUTTON)