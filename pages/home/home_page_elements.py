from selenium.webdriver.remote.webelement import WebElement

from utils.base_elements import BaseElements


class HomePageElements(BaseElements):

    def dismiss_btn(self):
        element = self.get_element("//*[text()='Dismiss']")
        self.flashlight_element(element)
        return element

    def side_menu_btn(self):
        element = self.get_element("//*[text()='menu']")
        self.flashlight_element(element)
        return element

    def logo_home_btn(self):
        element = self.get_element("//*[text()=' OWASP Juice Shop ']")
        self.flashlight_element(element)
        return element

    def search_btn(self):
        element = self.get_element("//*[text()=' search ']")
        self.flashlight_element(element)
        return element

    def account_btn(self):
        element = self.get_element("//*[@id='navbarAccount']")
        self.flashlight_element(element)
        return element

    def login_btn(self):
        element = self.get_element("//*[@id='navbarLoginButton']")
        self.flashlight_element(element)
        return element

    def basket_btn(self):
        element = self.get_element("//*[@aria-label='Show the shopping cart']")
        self.flashlight_element(element)
        return element

    def previous_page_btn(self):
        element = self.get_element("//*[@aria-label='Previous page']")
        self.flashlight_element(element)
        return element

    def next_page_btn(self):
        element = self.get_element("//*[@aria-label='Next page']")
        self.flashlight_element(element)
        return element


class ProductElements(BaseElements):

    def products_grid(self):
        element = self.get_elements("//*[@class='mat-grid-tile-content']")
        return element

    def open_product_details(self, elem: WebElement):
        element = self.get_elements("//*[contains(@class,'product')]", ancestor=elem)
        return element

    def product_img(self, elem: WebElement):
        element = self.get_elements("//img", ancestor=elem)
        return element

    def product_name_lbl(self, elem: WebElement):
        element = self.get_elements("//*[@class='item-name']", ancestor=elem)
        return element

    def product_price_lbl(self, elem: WebElement):
        element = self.get_elements("//*[@class='item-price']//span", ancestor=elem)
        return element

    def add_to_basket_btn(self, elem: WebElement):
        element = self.get_elements("//*[@class='mat-grid-tile-content']", ancestor=elem)
        return element


class ExtendedProductInfoElements(BaseElements):

    def product_container(self):
        element = self.get_element("//mat-dialog-container")
        self.flashlight_element(element)
        return element

    def product_img(self, elem):
        element = self.get_element("//*[@class='img-thumbnail']", ancestor=elem)
        self.flashlight_element(element)
        return element

    def product_title(self):
        element = self.get_element("/../following-sibling::div/h1", ancestor=self.product_img())
        self.flashlight_element(element)
        return element

    def product_description(self, elem):
        element = self.get_element("/../following-sibling::div/div", ancestor=self.product_img())
        self.flashlight_element(element)
        return element

    def product_price(self, elem):
        element = self.get_element("//*[@class='item-price']", ancestor=elem)
        self.flashlight_element(element)
        return element

    def open_close_reviews_button(self, elem):
        element = self.get_element("//*[contains(@class,'mat-expansion-indicator')]", ancestor=elem)
        self.flashlight_element(element)
        return element

    def comments(self, elem):
        element = self.get_element("//*[contains(@class,'comment')]", ancestor=elem)
        self.flashlight_element(element)
        return element

    def review_input(self, elem):
        element = self.get_element("//*[contains(@aria-label,'Text field to review a product')]", ancestor=elem)
        self.flashlight_element(element)
        return element

    def close_btn(self, elem):
        element = self.get_element("//*[@aria-label='Close Dialog']", ancestor=elem)
        self.flashlight_element(element)
        return element

    def submit_btn(self, elem):
        element = self.get_element("//*[@id='submitButton']", ancestor=elem)
        self.flashlight_element(element)
        return element
