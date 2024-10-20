import pytest
import random
import string
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@allure.title('Фикстура для инициализации и закрытия браузера')
@allure.description(
    'Фикстура будет инициализировать выбранный браузер (Firefox или Chrome) и закрывать его после завершения тестов')
@pytest.fixture(scope="class", params=["chrome", "firefox"])
def setup_driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def email():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + '@gmail.com'

@pytest.fixture
def password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))


@pytest.fixture
def name():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))


@pytest.fixture
def reference(password, email, name):
    reference = {
        'password': password,
        'email': email,
        'name': name
    }
    return reference