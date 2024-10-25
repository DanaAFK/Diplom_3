import allure
from data import Data
from page_object.base_page import BasePage
from locators.profile_locators import ProfileLocators as ProfLoc
from locators.login_locators import LoginLocator as LogLoc
from conftest import reference
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):

    @allure.title('Проверка наличия элементов на открытой странице')
    def open_page_check(self):
        self.visibility_of_element(By.XPATH, ProfLoc.ACCOUNT_BUTTON)
        return self.exist_check((By.XPATH, ProfLoc.ACCOUNT_BUTTON))

    @allure.title('Открытие страницы "История заказов"')
    def open_history_page(self):
        self.visibility_of_element(By.XPATH, ProfLoc.HISTORY_BUTTON)
        history_button = self.visibility_of_element(By.XPATH, ProfLoc.HISTORY_BUTTON)
        self.driver.execute_script('arguments[0].click();', history_button)
        if self.get_url() == Data.URL + Data.HISTORY_PAGE:
            return True
        else:
            return False

    @allure.title("Проверка наличия идентификатора заказа в истории")
    def found_order_at_history(self, order_id):
        elements = self.wait_all_elements((By.XPATH, ProfLoc.ORDERS_HISTORY))
        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.title('Нажатие кнопки "Выход" с проверкой выхода')
    def exit(self):
        exit_button = self.visibility_of_element(By.XPATH, ProfLoc.EXIT_BUTTON)
        self.driver.execute_script('arguments[0].click();', exit_button)
        self.visibility_not_of_element(By.XPATH, ProfLoc.EXIT_BUTTON)
        if self.get_url() == Data.URL + Data.LOGIN:
            return True
        else:
            return False

    @allure.title('Авторизация')
    def authorization(self, reference):
        name = reference['name']
        password = reference['password']
        email = reference['email']
        self.open_page(Data.URL + Data.REGISTER)
        self.visibility_of_element(By.XPATH, LogLoc.NAME_REG)
        self.wait_and_text((By.XPATH, LogLoc.NAME_REG), name)
        self.wait_and_text((By.XPATH, LogLoc.EMAIL_REG), email)
        self.wait_and_text((By.XPATH, LogLoc.PASSWORD_REG), password)
        self.click_element_if_clickable((By.XPATH, LogLoc.REG_BUTTON))
        self.visibility_not_of_element(By.XPATH, LogLoc.REG_BUTTON)
        self.visibility_of_element(By.XPATH, LogLoc.EMAIL_LOGIN)
        self.wait_and_text((By.XPATH, LogLoc.EMAIL_LOGIN), email)
        self.wait_and_text((By.XPATH, LogLoc.PASSWORD_LOGIN), password)
        self.click_element_if_clickable((By.XPATH, LogLoc.LOG_BUTTON))
        self.visibility_not_of_element(By.XPATH, LogLoc.LOG_BUTTON)

    @allure.title('Прекод')
    def precondition_for_tests(self, reference):
        self.authorization(reference)
        self.click_element_if_clickable((By.XPATH, ProfLoc.ACCOUNT_BUTTON))