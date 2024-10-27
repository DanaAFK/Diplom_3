import allure

from page_object.profile_page import ProfilePage
from locators.profile_locators import ProfileLocators as ProfileLoc
from conftest import driver, reference


class TestPersonal:

    @allure.title('зайти в "Личный кабинет"')
    def test_open_profile_page(self, driver, reference):
        profile = ProfilePage(driver)
        profile.authorization(reference)
        profile.click_element_if_clickable(ProfileLoc.ACCOUNT_BUTTON)
        assert profile.check_element_page() is True

    @allure.title('зайти на страницу "История заказов"')
    def test_open_history_page(self, driver, reference):
        profile = ProfilePage(driver)
        profile.precondition(reference)
        assert profile.history_page() is True

    @allure.title('выход из аккаунта на кнопку "Выйти"')
    def test_out_button(self, driver, reference):
        profile = ProfilePage(driver)
        profile.precondition(reference)
        assert profile.exit() is True
