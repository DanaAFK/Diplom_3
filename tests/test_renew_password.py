import allure
from locators.login_locators import LoginLocators
from page_object.login_page import LoginPage

from locators.renew_locators import RenewLocators as RenewLoc
from page_object.renew_page import RenewPage

from conftest import driver, reference


class TestRenewPassword:
    @allure.title('открыть страницу "Восстановление пароля"')
    def test_open_renew_page(self, driver):
        login = LoginPage(driver)
        login.login_page()
        login.click_element_if_clickable(LoginLocators.RENEW_PASSWORD_BUTTON)
        renew = RenewPage(driver)
        assert renew.logo_check() is True

    @allure.title('ввести почту. Нажать на кнопку "Восстановить"')
    def test_click_renew_password_with_email(self, driver, reference):
        renew = RenewPage(driver)
        renew.open_forgot_password()
        renew.write_email(reference)
        renew.click_element_if_clickable(RenewLoc.RENEW_BUTTON)
        assert renew.exist_password_field() is True

    @allure.step('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_show_hide_button(self, driver, reference):
        renew = RenewPage(driver)
        renew.precondition_in_renew(reference)
        renew.write_password(reference)
        renew.click_element_if_visible(RenewLoc.HIDE_OR_SHOW)
        assert (renew.status_circuit_password_field() is True and renew.status_password_field() is True)
