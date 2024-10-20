class RenewLocators:

    RENEW_PASSWORD_LOGO = '//*[text() = "Восстановление пароля"]'
    EMAIL = '//*[@name = "name"]'
    NEW_PASSWORD = '//*[@name="Введите новый пароль"]'
    STROKE_ACTIVE_PASSWORD = ".//div[contains(@class,'input_status_active')]"
    ACTIVE_PASSWORD = ".//label[contains(@class,'input__placeholder-focused')]"
    SHOW_HIDE_BUTTON = ".//div[contains(@class, 'input__icon')]/*[name()='svg']"
    RENEW_BUTTON = '//*[text() = "Восстановить"]'
