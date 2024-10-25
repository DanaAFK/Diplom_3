import allure
from page_object.base_page import BasePage
from data import Data
from locators.order_locators import OrderLocators as OrdLoc
from selenium.webdriver.common.by import By


class OrderListPage(BasePage):

    @allure.title('Переход в "Лента заказов"')
    def open_page(self):
        self.open_page(Data.URL + Data.REGISTER)

    @allure.title('Наличие в ленте идентификатора заказа')
    def found_order_at_list(self, order_id):
        elements = self.wait_all_elements((By.XPATH, OrdLoc.ORDERS_LIST))
        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.title('Открыть окно заказа')
    def order_window_check(self):
        return self.presence_check((By.XPATH, OrdLoc.COMPOUND)).is_displayed()

    @allure.title('Получить количество заказов за сегодня')
    def get_total_count_today(self):
        self.visibility_of_element(By.XPATH, OrdLoc.COUNT_TODAY)
        return self.wait_get_text((By.XPATH, OrdLoc.COUNT_TODAY))

    @allure.title("Получить общее кол-во заказов за всё время")
    def get_total_orders_count(self):
        self.visibility_of_element(By.XPATH, OrdLoc.COUNT_TOTAL)
        return self.wait_get_text((By.XPATH, OrdLoc.COUNT_TOTAL))

    @allure.title("Получение ID последнего оформленного заказа")
    def get_order_id(self):
        order_text = self.visibility_of_element(By.XPATH, OrdLoc.ORDER_INFO).text
        return order_text.split('#')[-1].strip()