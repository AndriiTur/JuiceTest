from pages.login_form.login_form_elements import LoginFormElements
from test_data import TestData
from utils.base_methods import BaseMethods

URL = 'http://localhost:3000/#/'


class LoginForm(BaseMethods):

    def __init__(self, driver, url=None):
        super().__init__(driver)
        self.driver = driver
        self.lf_elements: LoginFormElements = LoginFormElements(driver=self.driver)

        self.url = URL if url is None else url

    def login_default_user(self):
        print(TestData.USER)
        print(TestData.PASSWORD)
        self.type(self.lf_elements.email_input_field(), TestData.USER)
        self.type(self.lf_elements.pass_input_field(), TestData.PASSWORD)
        self.click(self.lf_elements.remember_me_cb())
        self.click(self.lf_elements.log_in_btn())
