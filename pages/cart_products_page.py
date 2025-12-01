from selenium.webdriver.common.by import By
from pages.base_class import BaseClass
from .cart_item import CartItem

class CartProductsPage(BaseClass):
    cart_item = (By.CSS_SELECTOR, ".cart_item")
    continue_shopping_btn = (By.CSS_SELECTOR, "#continue-shopping")
    checkout_btn = (By.CSS_SELECTOR, "#checkout")

    
    def __init__(self, browser):
        super().__init__(browser)

    def find_products(self) -> list['CartItem']:
        elements = self._find_many(self.cart_item)
        items = []
        for el in elements:
            items.append(CartItem(self.browser, el))
        return items
    
    def count_products(self):
        products = self.find_products()
        return len(products)
    
    def find_product_by_name(self, name: str):
        if name is None:
            raise ValueError("product name cannot be None")
        
        products = self.find_products()

        for product in products:
            if product.get_product_name() == name:
                return product
        
        return None
    
    def click_continue_shopping(self):
        self._click(self.continue_shopping_btn)

    def click_checkout(self):
        checkout_button = self._find(self.checkout_btn)
        self._click(checkout_button)
