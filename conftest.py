import pytest
import allure

from selenium import webdriver
from data import Data
from for_registration import password, name, email


@allure.title('Фикстура для инициализации и закрытия браузера')
@allure.description(
    'Фикстура инициализирует выбранный браузер (Firefox или Chrome) для каждого теста и закрывает его после завершения')
@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    browser = None
    try:
        if request.param == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--window-size=1920,1080')
            browser = webdriver.Firefox(options=options)
        elif request.param == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--window-size=1920,1080')
            browser = webdriver.Chrome(options=options)

        # Установка начальной страницы
        browser.get(Data.URL)
        yield browser

    except WebDriverException as e:
        pytest.fail(f"Ошибка при инициализации браузера: {e}")

    finally:
        if browser:
            browser.quit()


@pytest.fixture
def reference():
    references = {
        'password': password(),
        'email': email(),
        'name': name()
    }

    return references


