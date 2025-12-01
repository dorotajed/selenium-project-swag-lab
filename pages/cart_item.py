from selenium.webdriver.common.by import By
from pages.base_class import BaseClass


class CartItem(BaseClass):
    item_name = (By.CLASS_NAME, "inventory_item_name")
    item_desc = (By.CLASS_NAME, "inventory_item_desc")
    item_price = (By.CLASS_NAME, "inventory_item_price")
    item_quantity = (By.CLASS_NAME, "cart_quantity")
    remove_button = (By.CSS_SELECTOR, ".btn.btn_secondary.btn_small.cart_button")
    

    def __init__(self, browser, webelement):
        super().__init__(browser)
        self.element = webelement
    
    def get_price(self):
        price_text =  self.element.find_element(*self.item_price).text
        price = price_text.replace("$", "")
        return float(price)
    
    def get_product_name(self):
        return self.element.find_element(*self.item_name).text
    
    def get_item_quantity(self):
        return self.element.find_element(*self.item_quantity).text
    
    def remove_item(self):
        self.element.find_element(*self.remove_button).click()

    