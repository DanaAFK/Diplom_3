from page_object.base_page import BasePage
from data import Data
import allure


class LoginPage(BasePage):

    @allure.title('открыть страницу "Вход"')
    def login_page(self):
        self.open_page(f"{Data.URL}{Data.LOGIN}")