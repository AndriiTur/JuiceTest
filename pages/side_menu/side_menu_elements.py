from utils.base_elements import BaseElements


class SideMenuElements(BaseElements):

    def customer_feedback_lnk(self):
        element = self.get_element("//*[text()='menu']")
        self.flashlight_element(element)
        return element

    def complain_lnk(self):
        element = self.get_element("//*[text()='menu']")
        self.flashlight_element(element)
        return element

    def support_chat_lnk(self):
        element = self.get_element("//*[text()='menu']")
        self.flashlight_element(element)
        return element

    def About_us_lnk(self):
        element = self.get_element("//*[text()='menu']")
        self.flashlight_element(element)
        return element

    def photo_wall_lnk(self):
        element = self.get_element("//*[text()='menu']")
        self.flashlight_element(element)
        return element

    def membership_lnk(self):
        element = self.get_element("//*[text()='menu']")
        self.flashlight_element(element)
        return element

    def help_getting_started_lnk(self):
        element = self.get_element("//*[text()='menu']")
        self.flashlight_element(element)
        return element

    def git_hub(self):
        element = self.get_element("//*[text()='menu']")
        self.flashlight_element(element)
        return element
