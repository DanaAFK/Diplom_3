import allure
import time

from locators.home_locators import HomeLocator as HomLoc
from page_object.home_page import HomePage

from locators.order_locators import OrderLocators as OrderLoc
from page_object.order_page import OrderPage

from locators.profile_locators import ProfileLocators as ProfileLoc
from page_object.profile_page import ProfilePage

from conftest import driver, reference


class TestOrderList:

    @allure.title('id в ленте заказов и в истории заказов идентичны')
    def test_order_id_is_list_id(self, driver, reference):
        profile = ProfilePage(driver)
        order = OrderPage(driver)
        home = HomePage(driver)

        profile.authorization(reference)
        home.add_ingredient()
        home.click_element_if_clickable(HomLoc.ORDER_BUTTON)
        order_id = home.get_order_id()
        home.click_element_if_clickable(HomLoc.CLOSE_BUTTON)
        profile.click_element_if_clickable(ProfileLoc.ACCOUNT_BUTTON)
        profile.history_page()
        id_in_history = profile.order_id_history(order_id)
        home.click_element_if_clickable(HomLoc.LIST_OF_ORDER_BUTTON)
        id_in_list_order = order.found_order_at_list(order_id)
        assert id_in_history and id_in_list_order is True

    @allure.title('открыть страницу информации о заказе')
    def test_open_order_page(self, driver):
        order = OrderPage(driver)
        order.order_list()
        order.click_element_if_clickable(OrderLoc.ORDER_HISTORY)
        return order.open_orders()

    @allure.title('счетчика заказов за сегодня изменён после оформления заказа')
    def test_today_orders_counter(self, driver, reference):
        profile = ProfilePage(driver)
        order = OrderPage(driver)
        home = HomePage(driver)

        profile.authorization(reference)
        home.click_element_if_clickable(HomLoc.LIST_OF_ORDER_BUTTON)
        pre_count = int(order.get_total_count_today())

        home.click_element_if_clickable(HomLoc.CONSTRUCTOR_BUTTON)
        home.add_ingredient()
        home.click_element_if_clickable(HomLoc.ORDER_BUTTON)
        home.click_element_if_clickable(HomLoc.CLOSE_BUTTON)

        home.click_element_if_clickable(HomLoc.LIST_OF_ORDER_BUTTON)

        post_count = int(order.get_total_count_today())
        attempts = 4
        while post_count == pre_count and attempts > 0:
            time.sleep(1)
            post_count = int(order.get_total_count_today())
            attempts -= 1
        assert post_count > pre_count

    @allure.title('созданый заказ появится в ленте заказов')
    def test_new_order_id_in_list_order(self, driver, reference):
        profile = ProfilePage(driver)
        order = OrderPage(driver)
        home = HomePage(driver)

        profile.authorization(reference)
        home.add_ingredient()
        home.click_element_if_clickable(HomLoc.ORDER_BUTTON)
        order_id = home.get_order_id()
        home.click_element_if_clickable(HomLoc.CLOSE_BUTTON)
        home.click_element_if_clickable(HomLoc.LIST_OF_ORDER_BUTTON)
        assert order.found_order_at_list(order_id) is True