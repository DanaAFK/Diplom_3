from selenium.webdriver.common.by import By


class ProfileLocators:

    HISTORY_OF_ORDER = (By.XPATH, "//div[contains(@class, 'OrderHistory_orderHistory__')]")
    HISTORY_BUTTON = (By.XPATH, '//*[@href = "/account/order-history"]')
    ACCOUNT_BUTTON = (By.XPATH, '//*[@href = "/account"]')
    ACCOUNT_PROFILE_BUTTON = (By.XPATH, '//*[@href="/account/profile"]')

    EXIT_BUTTON = (By.XPATH, '//*[@href="/account/order-history"]/following::*[@type="button"][1]')


