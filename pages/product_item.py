from selenium.webdriver.common.by import By

class ProductItem:
    inventory_item_name = (By.CSS_SELECTOR, ".inventory_item_name")
    inventory_item_desc = (By.CLASS_NAME, "inventory_item_desc")
    inventory_item_price = (By.CLASS_NAME, "inventory_item_price")
    add_to_cart_button = (By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory")


    def __init__(self, browser, web_element):
        self.browser = browser
        self.element = web_element

    def get_product_name(self):
        return self.element.find_element(*self.inventory_item_name).text
    
    def get_product_price(self) -> float:
        price_text = self.element.find_element(*self.inventory_item_price).text
        price = price_text.replace("$", "")
        return float(price)
    
    def product_description_is_displayed(self):
        return self.element.find_element(*self.inventory_item_desc).is_displayed()
    
    def click_add_to_cart_button(self):
        self.element.find_element(*self.add_to_cart_button).click()
        
