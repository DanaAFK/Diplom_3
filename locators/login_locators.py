from selenium.webdriver.common.by import By


class LoginLocators:

    RENEW_PASSWORD_BUTTON = (By.XPATH, '//*[text() = "Восстановить пароль"]')
    GO = (By.XPATH, '//button[text()="Войти"]')
    REG_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')

    EMAIL_LOGIN = (By.XPATH, '//*[@name = "name"]')
    EMAIL_LOGIN_2 = (By.XPATH, '//input[@name="name" and contains(@class, "input_textfield")]')
    PASSWORD_LOGIN = (By.XPATH, '//*[@name = "Пароль"]')

    NAME_REG = (By.XPATH, '//*[text()="Регистрация"]//following::*[@name="name"][1]')
    EMAIL_REG = (By.XPATH, '//*[text()="Регистрация"]/following::*[@name="name"][2]')
    PASSWORD_REG = (By.XPATH, '//input[@name="Пароль" and @type="password"]')

