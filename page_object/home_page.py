import allure
from page_object.base_page import BasePage
from data import Data
from locators.home_locators import HomeLocator as HomLoc
from locators.order_locators import OrderLocators as OrdLoc
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    @allure.title('Переход на страницу регистрации')
    def open_reg_page(self):
        self.open_page(Data.URL + Data.REGISTER)

    @allure.title('Переход на главную страницу')
    def open_home_page(self):
        self.open_page(Data.URL)

    @allure.title('Переход после нажатия на кнопку "Лента Заказов"')
    def check_order_list(self):
        return self.exist_check((By.XPATH, OrdLoc.ORDER_PAGE_LOGO))

    @allure.title('Переход после нажатия на кнопку "Конструктор"')
    def constructor_check(self):
        return self.exist_check((By.XPATH, HomLoc.CONSTRUCTOR_LOGO))

    @allure.title('Преход в окно ингредиента')
    def clickable_order_button_check(self):
        return self.element_clickable((By.XPATH, HomLoc.INGREDIENT_WINDOW_LOGO)) is not None

    @allure.title('Предусловие: открытие главной страницы, открытие окна ингредиента')
    def precondition_for_closing_window(self):
        self.open_home_page()
        self.click_element_if_clickable((By.XPATH, HomLoc.F_BUN_BUTTON))

    @allure.title('Получить значения счетчика ингредиента')
    def get_count_value(self):
        return self.wait_get_text((By.XPATH, HomLoc.INGREDIENT_COUNTER))

    @allure.title('Перетаскивание ингредиента')
    def add_ingredient_to_order(self):
        self.element_clickable(By.XPATH.HomLoc.F_BUN_BUTTON)
        self.drag_and_drop((By.XPATH, HomLoc.F_BUN_BUTTON), (By.XPATH, HomLoc.ORDERS_PACK))

    @allure.title('Получить текста из окна с информацией об оформленном заказе')
    def placing_order_text_check(self):
        self.visibility_of_element(By.XPATH, HomLoc.ORDER_ID_TEXT)
        return self.wait_get_text((By.XPATH, HomLoc.ORDER_ID_TEXT))

    @allure.title('Получить id заказа')
    def get_order_id(self):
        self.visibility_of_element(By.XPATH, HomLoc.ORDER_ID_TEXT)
        order_id = self.wait_get_text((By.XPATH, HomLoc.ORDER_ID))
        while order_id == '12345':
            order_id = self.wait_get_text((By.XPATH, HomLoc.ORDER_ID))
        return f"{order_id}"
