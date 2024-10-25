import pytest
import random
import string
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from data import Data


@allure.title('Фикстура для инициализации и закрытия браузера')
@allure.description(
    'Фикстура будет инициализировать выбранный браузер (Firefox или Chrome) и закрывать его после завершения тестов')
@pytest.fixture(scope="class", params=["chrome", "firefox"])
def driver(request):
    browser = None
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        browser = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        browser = webdriver.Chrome(options=options)
    browser.get(Data.URL)
    yield browser
    browser.quit()


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