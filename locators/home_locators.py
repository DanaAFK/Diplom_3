from selenium.webdriver.common.by import By


class HomeLocator:

    CONSTRUCTOR_LOGO = (By.XPATH, '//*[text() = "Соберите бургер"]')
    INGREDIENT_WINDOW_LOGO = (By.XPATH, '//*[text() = "Детали ингредиента"]')

    CONSTRUCTOR_BUTTON = (By.XPATH, '//*[text() = "Конструктор"]')
    LIST_OF_ORDER_BUTTON = (By.XPATH, '//p[contains(.,"Лента Заказов")]')
    ORDER_BUTTON = (By.XPATH, '//*[text()="Оформить заказ"]')
    F_BUN_BUTTON = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    CLOSE_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')

    ID_TEXT = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_ID = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')

    COUNTER_INGREDIENTS = (By.XPATH, './/p[contains(@class, "counter_counter")]')
    PACK = (By.XPATH, '//li[2][contains(@class, "BurgerConstructor_basket__listItem")]')