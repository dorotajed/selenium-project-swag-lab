from selenium.webdriver.common.by import By
from pages.base_class import BaseClass

class CheckoutPage(BaseClass):

    #checkout overview page
    product_name = (By.CLASS_NAME, "inventory_item_name")
    product_price = (By.CLASS_NAME, "inventory_item_price")
    subtotal_price = (By.CLASS_NAME, "summary_subtotal_label")
    finish_btn = (By.CSS_SELECTOR, "#finish")
    completed_order_msg = (By.CSS_SELECTOR, "[data-test='complete-header']")


    def __init__(self, browser):
        super().__init__(browser)
    

    def get_product_name(self):
        self._find(self.product_name)
        return self._find(self.product_name).text
    
    def get_product_price(self):
        self._find(self.product_price)
        price_text =  self._find(self.product_price).text
        price = price_text.replace("$", "")
        return float(price)
    
    def get_subtotal_price(self):
        self._find(self.subtotal_price)
        price_text = self._find(self.subtotal_price).text
        price = price_text.split("$")[1]
        return float(price)

    def click_finish(self):
        finish_button = self._find(self.finish_btn)
        self._click(finish_button)

    def completed_order_notification_is_displayed(self):
        return self._find(self.completed_order_msg).is_displayed()