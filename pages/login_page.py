from selenium.webdriver.common.by import By
from pages.base_class import BaseClass

from pages.products_page import ProductsPage

class LoginPage(BaseClass):
    username_field = (By.CSS_SELECTOR, "#user-name")
    password_field = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "#login-button")
    error_message_container = (By.CSS_SELECTOR, "[data-test='error']")


    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self, page_url):
        self.browser.get(page_url)

    def attempt_login(self, username, password):
        self._find(self.username_field).send_keys(username)
        self._find(self.password_field).send_keys(password)
        self._find(self.login_button).click()
        return ProductsPage(self.browser)

    def get_error_message(self):
        element = self._find(self.error_message_container)
        return self._get_text(element)
        
