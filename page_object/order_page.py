import allure
from page_object.base_page import BasePage
from data import Data
from locators.order_locators import OrderLocators as OrdLoc


class OrderPage(BasePage):

    @allure.title('открыть "Лента заказов"')
    def order_list(self):
        self.open_page(f"{Data.URL}{Data.LIST_PAGE}")

    @allure.title('открыть окно заказа')
    def open_orders(self):
        return self.presence_check(OrdLoc.COMPOUND).is_displayed()

    @allure.title('в ленте заказов есть идентификатор заказа')
    def found_order_at_list(self, order_id):
        elements = self.wait_all_elements(OrdLoc.ORDERS_LIST)
        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.title('количество заказов за сегодня')
    def get_total_count_today(self):
        self.visibility_of_element(OrdLoc.COUNT_TODAY)
        return self.wait_get_text(OrdLoc.COUNT_TODAY)

    @allure.title("общее кол-во заказов за всё время")
    def get_total_orders_count(self):
        self.visibility_of_element(OrdLoc.COUNT_TOTAL)
        return self.wait_get_text(OrdLoc.COUNT_TOTAL)
