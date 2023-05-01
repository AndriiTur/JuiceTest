from utils.base_elements import BaseElements


class RegisterFormElements(BaseElements):

    def email_input_field(self):
        element = self.get_element("//*[@id='emailControl']")
        self.flashlight_element(element)
        return element

    def password_input_field(self):
        element = self.get_element("//*[@id='passwordControl']")
        self.flashlight_element(element)
        return element

    def password_confirm_input_field(self):
        element = self.get_element("//*[@id='repeatPasswordControl']")
        self.flashlight_element(element)
        return element

    def show_hide_password_advise_cb(self):
        element = self.get_element("//*[@class='mat-slide-toggle-bar']")
        self.flashlight_element(element)
        return element

    def security_question_dd_btn(self):
        element = self.get_element("//*[contains(@class,'mat-select-arrow-wrapper')]")
        self.flashlight_element(element)
        return element

    def security_question_options(self):
        element = self.get_elements("//mat-option")
        self.flashlight_element(element)
        return element

    def security_question_answer(self):
        element = self.get_elements("//*[@id='securityAnswerControl']")
        self.flashlight_element(element)
        return element

    def submit_register_btn(self):
        element = self.get_element("//*[@id='registerButton']")
        self.flashlight_element(element)
        return element
