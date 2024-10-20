from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def drag_and_drop(self, one, two):
        drag = self.driver.find_element(*one)
        drop = self.driver.find_element(*two)
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()

    def open_page(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.url

    def wait_and_text(self, locator, text):
        element = self.visibility_of_element(locator)
        element.send_keys(text)

    def wait_get_text(self, locator):
        element = self.visibility_of_element(locator)
        return element.text

    def visibility_of_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def visibility_not_of_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator))

    def exist_check(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def presence_check(self, locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element_if_visible(self, locator):
        element = self.visibility_of_element(locator)
        element.click()

    def click_element_if_clickable(self, locator):
        click_element = self.visibility_of_element(locator)
        self.driver.execute_script('arguments[0].click();', click_element)

    def wait_all_elements(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(locator))

    def invisibility_check(self, locator) -> object:
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))