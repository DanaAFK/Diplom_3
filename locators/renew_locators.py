from selenium.webdriver.common.by import By


class RenewLocators:

    RENEW_PASSWORD_LOGO = By.XPATH, '//*[text() = "Восстановление пароля"]'
    RENEW_BUTTON = By.XPATH, '//*[text() = "Восстановить"]'

    EMAIL = By.XPATH, '//*[@name = "name"]'
    NEW_PASSWORD = By.XPATH, '//*[@name="Введите новый пароль"]'
    ACTUAL_PASSWORD_FIELD = By.XPATH, ".//div[contains(@class,'input_status_active')]"
    ACTUAL_PASSWORD = By.XPATH, ".//label[contains(@class,'input__placeholder-focused')]"
    HIDE_OR_SHOW = By.XPATH, ".//div[contains(@class, 'input__icon')]/*[name()='svg']"

