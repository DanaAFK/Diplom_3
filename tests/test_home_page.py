import allure

from locators.home_locators import HomeLocator as HomLoc
from page_object.home_page import HomePage
from page_object.profile_page import ProfilePage
from conftest import driver, reference


class TestHomePage:

    @allure.title('открыть страницу "Конструктор"')
    def test_open_constructor_page(self, driver):
        home = HomePage(driver)
        home.registration_page()
        home.click_element_if_clickable(HomLoc.CONSTRUCTOR_BUTTON)
        assert home.constructor_check() is True

    @allure.title('открыть страницу "Лента заказов"')
    def test_open_list_orders_page(self, driver):
        home = HomePage(driver)
        home.registration_page()
        home.click_element_if_clickable(HomLoc.LIST_OF_ORDER_BUTTON)
        assert home.check_order_list() is True

    @allure.title('открыть окно детали ингредиентов')
    def test_open_ingredients(self, driver):
        home = HomePage(driver)
        home.home_page()
        home.click_element_if_clickable(HomLoc.F_BUN_BUTTON)
        assert home.clickable_order_button_check() is True

    @allure.title('закрыть окно деталей по кнопке')
    def test_close_ingredients_page(self, driver):
        home = HomePage(driver)
        home.precondition_for_closing_window()
        home.click_element_if_clickable(HomLoc.CLOSE_BUTTON)
        assert home.clickable_order_button_check() is True

    @allure.title('перетаскивание ингредиента в пак')
    def test_add_ingredient_on_pack(self, driver):
        home = HomePage(driver)
        home.home_page()
        before = home.get_count_value()
        home.wait_for_bun_button_to_appear()
        home.add_ingredient()
        after = home.get_count_value()
        assert before == '0'
        assert after == '2'

    @allure.title('можно оформить заказ авторизованным пользователем')
    def test_make_order_authorized_success(self, driver, reference):
        home = HomePage(driver)
        profile = ProfilePage(driver)

        profile.authorization(reference)
        home.add_ingredient()
        home.click_element_if_clickable(HomLoc.ORDER_BUTTON)
        assert home.order_text_check() == 'идентификатор заказа'

