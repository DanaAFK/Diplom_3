from selenium.webdriver.common.by import By


class OrderLocators:

    ORDER_PAGE_LOGO = (By.XPATH, '//*[text() = "Лента заказов"]')

    ORDER_HISTORY = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')
    COMPOUND = (By.XPATH, '//*[text()="Cостав"]')
    ORDERS_LIST = (By.XPATH, '//p[1][contains(@class, "text_type_digits-default")]')

    COUNT_TODAY = (By.XPATH, '//*[text() = "Выполнено за сегодня:"]/following::*[@class][1]')
    COUNT_TOTAL = (By.XPATH, "//*[contains(text(), 'Выполнено за все время')]/following-sibling::span")
