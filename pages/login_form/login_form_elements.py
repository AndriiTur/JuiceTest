from utils.base_elements import BaseElements


class LoginFormElements(BaseElements):
    def email_input_field(self):
        element = self.get_element("//*[@id='email']")
        self.flashlight_element(element)
        return element

    def pass_input_field(self):
        element = self.get_element("//*[@id='password']")
        self.flashlight_element(element)
        return element

    def remember_me_cb(self):
        element = self.get_element("//*[@class='mat-checkbox-inner-container']")
        self.flashlight_element(element)
        return element

    def log_in_btn(self):
        element = self.get_element("//*[@id='loginButton']")
        self.flashlight_element(element)
        return element

    def register_btn(self):
        element = self.get_element("//*[@class='primary-link']")
        self.flashlight_element(element)
        return element
