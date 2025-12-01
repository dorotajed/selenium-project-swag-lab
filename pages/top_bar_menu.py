from selenium.webdriver.common.by import By
from pages.base_class import BaseClass


class TopBarMenu(BaseClass):
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, browser):
        super().__init__(browser)

    def get_product_quantity(self):
        return self._get_text(self.cart_badge)
    
    def click_icon(self):
        self._click(self.cart_icon)