import allure
from selenium.webdriver.common.by import By
from page_object.home_page import HomePage
from locators.home_locators import HomeLocator as HomLoc
from conftest import driver


class TestHomePage:

    @allure.title('Открыть страницу "Конструктор"')
    def test_open_constructor_page(self, driver):
        home = HomePage(driver)
        home.open_reg_page()
        home.click_element_if_clickable((By.XPATH, HomLoc.CONSTRUCTOR_BUTTON))
        assert home.constructor_check() is True

    @allure.title('Открыть страницу "Лента заказов"')
    def test_open_order_list_page(self, driver):
        home = HomePage(driver)
        home.open_reg_page()
        home.click_element_if_clickable((By.XPATH, HomLoc.ORDER_LIST_BUTTON))
        assert home.check_order_list() is True

    @allure.title('Открыть окно детали ингредиентов')
    def test_open_ingredient_window(self, driver):
        home = HomePage(driver)
        home.open_home_page()
        home.click_element_if_clickable((By.XPATH, HomLoc.F_BUN_BUTTON))
        assert home.clickable_order_button_check() is True

    @allure.title('Закрыть окно деталей крестиком')
    def test_close_ingredient_window(self, driver):
        home = HomePage(driver)
        home.precondition_for_closing_window()
        home.click_element_if_clickable((By.XPATH, HomLoc.CLOSE_BUTTON))
        assert home.clickable_order_button_check() is True



