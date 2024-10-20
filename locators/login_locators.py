class Login:

    RESTORE_PASSWORD_BUTTON = '//*[text() = "Восстановить пароль"]'

    NAME_REG = '//*[text()="Регистрация"]/following::*[@name = "name"][1]'
    EMAIL_REG = '//*[text()="Регистрация"]/following::*[@name = "name"][2]'
    PASSWORD_REG = "//*[@name  = \"Пароль\"]"

    LOGIN_BUTTON =  '//button[text() = "Войти"]'

    REG_BUTTON = '//button[text() = "Зарегистрироваться"]'
    EMAIL_LOGIN = '//*[@name = "name"]'
    PASSWORDLOGIN = '//*[@name = "Пароль"]'
