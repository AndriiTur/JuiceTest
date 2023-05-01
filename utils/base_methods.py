import datetime
import logging
from time import sleep
from selenium.webdriver import ActionChains
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement

logger = logging.getLogger()
DEMO = True


class BaseMethods:
    """ Create this class for wrap elements handle errors and log errors with elements """
    start_timestamp = datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    logger.info(f"Start running tests: {start_timestamp}")

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_screenshots(self):
        logger.error("something went wrong((")
        self.driver.save_screenshots('here/will/be/path/to/file')
        return True

    def click(self, element: object) -> bool:
        self.highlight_element(element, for_demo=DEMO)
        element.click()
        return True

    def clear_text(self, element: object) -> bool:
        element.clear()
        return True

    def scroll_to_element(self, element: object) -> bool:
        ActionChains(self.driver).move_to_element(element).perform()
        self.highlight_element(element, for_demo=DEMO)
        return True

    def double_click(self, element: object) -> bool:
        self.highlight_element(element, for_demo=DEMO)
        ActionChains(self.driver).double_click(element).perform()
        return True

    def type(self, element: object, text) -> bool:
        self.click(element)
        self.clear_text(element)
        element.send_keys(text)
        return True

    def highlight_element(self, element: object, time=2, color='#F6F7AD', for_demo=False) -> bool:
        """ Highlight element if param True by default False """

        if for_demo:
            original_style: str = element.get_attribute('style')
            self.driver.execute_script(f"arguments[0].setAttribute('style', arguments[1])", element,
                                       f'border: 4px solid {color}')
            sleep(time)
            return True if self.driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element,
                                                      original_style) else False

    def is_displayed(self, element: object) -> bool:
        try:
            return element.is_displayed() if isinstance(element, WebElement) else False
        except (NoSuchElementException, TimeoutException, AttributeError):
            return False

    @staticmethod
    def wait_for_page(timer: float):
        # TODO wait for event page_load move to utils
        sleep(timer)
        return True
