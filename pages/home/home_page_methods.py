from pages.home.home_page_elements import HomePageElements
from pages.login_form.login_form_methods import LoginForm
from test_data import TestData
from utils.base_methods import BaseMethods

URL = 'http://localhost:3000/#/'


class HomePage(BaseMethods):

    def __init__(self, driver, url=None):
        super().__init__(driver)
        self.driver = driver
        self.elements: HomePageElements = HomePageElements(driver=self.driver)
        # self.product_elements: ProductElements = ProductElements(driver=self.driver)
        # self.pi_elements: ExtendedProductInfoElements = ExtendedProductInfoElements(driver=self.driver)
        # self.sm_elements: SideMenuElements = SideMenuElements(driver=self.driver)

        self.url = URL if url is None else url

        self.open_page(self.url)

    def open_page(self, url=None):
        if not url:
            url = self.url

        self.driver.get(url)

        return self

    def open_form_for_login(self):
        self.click(self.elements.dismiss_btn())
        self.click(self.elements.account_btn())
        self.click(self.elements.login_btn())
        return LoginForm(self.driver)

    def is_user_logged_in(self):
        self.wait_for_page(1)
        return self.is_displayed(self.elements.basket_btn())

