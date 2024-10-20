class OrderLocators:

    ORDER_PAGE_LOGO = '//*[text() = "Лента заказов"]'
    ORDER_HISTORY = '//*[contains(@class, "OrderHistory_link")]'
    COMPOUND = '//*[text()="Cостав"]'
    ORDERS_LIST = '//p[1][contains(@class, "text_type_digits-default")]'
    COUNT_TODAY = '//*[text() = "Выполнено за сегодня:"]/following::*[@class][1]'
    ALL_COUNT = "//*[text() = 'Выполнено за все время:'"