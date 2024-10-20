class ProfileLocators:

    ORDERS_HISTORY = "//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class,'text_type_digits-default')]"

    HISTORY_BUTTON = '//*[@href="/account/order-history"]'
    ACCOUNT_BUTTON = '//*[@href = "/account"]'
    ACCOUNT_PROFILE_BUTTON = '//*[@href="/account/profile"]'
    EXIT_BUTTON = '//*[@href="/account/order-history"]/following::*[@type="button"][1]'


