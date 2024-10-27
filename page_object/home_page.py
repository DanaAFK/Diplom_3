import allure
from page_object.base_page import BasePage
from data import Data
from locators.home_locators import HomeLocator as HomLoc
from locators.order_locators import OrderLocators as OrdLoc


class HomePage(BasePage):

    @allure.title('переидти на главную страницу')
    def home_page(self):
        self.open_page(Data.URL)

    @allure.title('открыть страницу регистрации')
    def registration_page(self):
        self.open_page(f"{Data.URL}{Data.REGISTER}")

    @allure.title('открыть окно ингредиента')
    def clickable_order_button_check(self):
        return self.element_clickable(HomLoc.INGREDIENT_WINDOW_LOGO) is not None

    @allure.title('открыть "Лента Заказов" по кнопке')
    def check_order_list(self):
        return self.exist_check(OrdLoc.ORDER_PAGE_LOGO)

    @allure.title('Переход после нажатия на кнопку "Конструктор"')
    def constructor_check(self):
        return self.exist_check(HomLoc.CONSTRUCTOR_LOGO)

    @allure.title('открыть главную страницу,открыть окно ингредиента')
    def precondition_for_closing_window(self):
        self.home_page()
        self.click_element_if_clickable(HomLoc.F_BUN_BUTTON)

    @allure.title('добавить ингредиенты')
    def add_ingredient(self):
        self.element_clickable(HomLoc.F_BUN_BUTTON)
        self.drag_and_drop(HomLoc.F_BUN_BUTTON, HomLoc.PACK)

    @allure.title('ожидание кнопки булки')
    def wait_for_bun_button_to_appear(self):
        self.wait_all_elements(HomLoc.F_BUN_BUTTON)

    def order_text_check(self):
        element = self.visibility_of_element(HomLoc.ID_TEXT, 15)
        return element.text

    @allure.title('получить id заказа')
    def get_order_id(self):
        self.visibility_of_element(HomLoc.ID_TEXT)
        order_id = self.wait_get_text(HomLoc.ORDER_ID)
        while order_id == '9999':
            order_id = self.wait_get_text(HomLoc.ORDER_ID)
        return f"{order_id}"

    @allure.title('получить значение счетчика ингредиента')
    def get_count_value(self):
        value = self.wait_get_text(HomLoc.COUNTER_INGREDIENTS)
        return value.strip()