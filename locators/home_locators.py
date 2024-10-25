class HomeLocator:

    GO_ACC_BUTTON = '//*[text() = "Войти в аккаунт"]'

    CONSTRUCTOR_BUTTON = '//*[text() = "Конструктор"]'
    ORDER_LIST_BUTTON = '//p[contains(.,"Лента Заказов")]'
    F_BUN_BUTTON = '//img[@alt="Флюоресцентная булка R2-D3"]'
    ORDER_BUTTON = '//*[text()="Оформить заказ"]'
    CLOSE_BUTTON = '//button[contains(@class,"close")]'

    CONSTRUCTOR_LOGO = '//*[text() = "Соберите бургер"]'
    ORDER_ID_TEXT = '//p[text()="идентификатор заказа"]'
    ORDER_ID = '//h2[contains(@class, "Modal_modal__title_shadow")]'
    INGREDIENT_WINDOW_LOGO = '//*[text() = "Детали ингредиента"]'
    INGREDIENT_COUNTER = './/p[contains(@class, "counter_counter")]'
    ORDERS_PACK = '//li[2][contains(@class, "BurgerConstructor_basket__listItem")]'
    ORDER_NUMBER_IN_PROGRESS =  "//p[contains(text(), '№')]"