from data import Data
from page_object.base_page import BasePage
from locators.profile_locators import ProfileLocators as ProfLoc
from locators.login_locators import LoginLocators as LogLoc

from selenium.common.exceptions import TimeoutException
import allure

from conftest import reference


class ProfilePage(BasePage):

    @allure.title('элементы есть на открытой странице')
    def check_element_page(self):
        self.visibility_of_element(ProfLoc.ACCOUNT_BUTTON)
        return self.exist_check(ProfLoc.ACCOUNT_BUTTON)

    @allure.title('открыть "История заказов"')
    def history_page(self):
        self.visibility_of_element(ProfLoc.HISTORY_BUTTON)
        history_button = self.visibility_of_element(ProfLoc.HISTORY_BUTTON)
        self.driver.execute_script('arguments[0].click();', history_button)
        if self.get_url() == Data.URL + Data.HISTORY_PAGE:
            return True
        else:
            return False

    @allure.title("наличие идентификатора заказа в истории")
    def order_id_in_history_(self, order_id):
        elements = self.wait_all_elements(ProfLoc.HISTORY_OF_ORDER)
        for element in elements:
            if order_id == element.text:
                return True

    @allure.title("наличие идентификатора заказа в истории(отладка)")
    def order_id_history(self, order_id):
        try:
            elements = self.wait_all_elements(ProfLoc.HISTORY_OF_ORDER)
            for element in elements:
                if order_id in element.text:
                    return True
            return False
        except TimeoutException:
            print("Elements not found within the timeout.")
            return False

    @allure.step('Авторизация')
    def authorization(self, reference):
        name = reference['name']
        password = reference['password']
        email = reference['email']
        self.open_page(f"{Data.URL}{Data.REGISTER}")

        self.visibility_of_element(LogLoc.NAME_REG)
        self.wait_and_text(LogLoc.NAME_REG, name)
        self.wait_and_text(LogLoc.EMAIL_REG, email)
        self.wait_and_text(LogLoc.PASSWORD_REG, password)
        self.click_element_if_clickable(LogLoc.REG_BUTTON)
        self.visibility_not_of_element(LogLoc.REG_BUTTON)

        self.visibility_of_element(LogLoc.EMAIL_LOGIN)
        self.wait_and_text(LogLoc.EMAIL_LOGIN, email)
        self.wait_and_text(LogLoc.PASSWORD_LOGIN, password)

        self.click_element_if_clickable(LogLoc.GO)
        self.visibility_not_of_element(LogLoc.GO)

    @allure.title('выход по кнопке "Выход"')
    def exit(self):
        exit_button = self.visibility_of_element(ProfLoc.EXIT_BUTTON)
        self.driver.execute_script('arguments[0].click();', exit_button)
        self.visibility_not_of_element(ProfLoc.EXIT_BUTTON)
        if self.get_url() == Data.URL + Data.LOGIN:
            return True
        else:
            return False

    @allure.title('Прекод')
    def precondition(self, reference):
        self.authorization(reference)
        self.click_element_if_clickable(ProfLoc.ACCOUNT_BUTTON)