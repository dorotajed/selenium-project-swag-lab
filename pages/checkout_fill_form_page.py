from selenium.webdriver.common.by import By
from pages.base_class import BaseClass

class CheckoutFillFormPage(BaseClass):
    first_name = (By.CSS_SELECTOR, "#first-name")
    last_name = (By.CSS_SELECTOR, "#last-name")
    postal_code = (By.CSS_SELECTOR, "#postal-code")
    continue_button = (By.CSS_SELECTOR, "#continue")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, browser):
        super().__init__(browser)

    def fill_checkout_form(self, firstname, lastname, postalcode):
        self._send_keys(self.first_name, firstname)
        self._send_keys(self.last_name, lastname)
        self._send_keys(self.postal_code, postalcode)

    def get_error_message(self):
        return self._get_text(self.error_message)
    
    def click_continue(self):
        self._click(self.continue_button)
