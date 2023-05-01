from pages.register_form.register_form_elements import RegisterFormElements
from test_data import TestData
from utils.base_methods import BaseMethods

URL = 'http://localhost:3000/#/'


class RegisterForm(BaseMethods):

    def __init__(self, driver, url=None):
        super().__init__(driver)
        self.driver = driver
        self.lf_elements: RegisterFormElements = RegisterFormElements(driver=self.driver)

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

    def login_default_user(self):
        self.open_form_for_login()

        self.type(self.lf_elements.email_input_field(), TestData.USER)
        self.type(self.lf_elements.pass_input_field(), TestData.PASSWORD)
        self.click(self.lf_elements.remember_me_cb())
        self.click(self.lf_elements.log_in_btn())

    def is_user_logged_in(self):
        self.wait_for_page(1)
        return self.is_displayed(self.elements.basket_btn())

