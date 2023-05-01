from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

from selenium.webdriver.remote.webelement import WebElement


class BaseElements:
    """ Create this class for wrap elements handle errors and log errors with elements """

    def __init__(self, driver) -> None:
        self.driver = driver

    def flashlight_element(self, element, demo=True):
        if demo:
            self.highlight_element(element, wait_seconds=1, color='#F6F7AD', demo=demo)
        return element

    def highlight_element(self, element: object, wait_seconds=1, color='#F6F7AD', demo=False):
        """Highlight element for DEMO"""

        if demo:
            original_style: str = element.get_attribute('style')
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element,
                                       f'border: 4px solid {color};')
            sleep(wait_seconds)
            return True if self.driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element,
                                                      original_style) else False

    def scroll_to_element(self, element: object):
        ActionChains(self.driver).move_to_element(element).perform()

    def is_displayed(self, element: object):
        return element.is_displayed() if isinstance(element, WebElement) else False

    def get_element(self, locator, ancestor: WebElement = None, by=By.XPATH):
        if ancestor:
            return ancestor.find_element(by, locator)
        return self.driver.find_element(by, locator)

    def get_elements(self, locator, ancestor: WebElement = None, by=By.XPATH):
        if ancestor:
            return ancestor.find_elements(by, locator)
        return self.driver.find_elements(by, locator)
