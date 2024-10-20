import allure
from page_object.base_page import BasePage
from data import Data


class LoginPage(BasePage):
    @allure.title('Открыть страницу "Вход"')
    def login_page(self):
        self.open_page(f'{Data.URL}{Data.LOGIN}')