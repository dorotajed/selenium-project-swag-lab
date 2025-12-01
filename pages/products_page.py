from selenium.webdriver.common.by import By
from .product_item import ProductItem
from pages.base_class import BaseClass

class ProductsPage(BaseClass):
    inventory_list = (By.CSS_SELECTOR, ".inventory_list")
    inventory_item = (By.CSS_SELECTOR, ".inventory_item")
    sorting_container = (By.CLASS_NAME, "product_sort_container")
    selected_sorting_option = (By.CLASS_NAME, "active_option")
    name_asc_sorting = (By.CSS_SELECTOR, "option[value='az']")
    name_desc_sorting = (By.CSS_SELECTOR, "option[value='za']")
    price_asc_sorting =(By.CSS_SELECTOR, "option[value='lohi']")
    price_desc_sorting =(By.CSS_SELECTOR, "option[value='hilo']")
    
    def __init__(self, browser):
        super().__init__(browser)

    def products_list_is_displayed(self) -> bool:
        return bool(self._find(self.inventory_list))

    def find_products(self) -> list[ProductItem]:
        elements = self._find_many(self.inventory_item)
        items = []
        for el in elements:
            items.append(ProductItem(self.browser, el))
        return items
    
    def count_products(self):
        products = self.find_products()
        return len(products)
    
    def find_product_by_name(self, name: list):
        if name is None:
            raise ValueError("product name cannot be None")
        
        products = self.find_products()

        for product in products:
            if product.get_product_name() == name:
                return product
        
        return None
    
    def get_selected_sorting_option(self):
        self._find(self.selected_sorting_option)
        return self.browser.find_element(*self.selected_sorting_option).text

    def _select_sorting_option(self, locator):
        dropdown = self._wait_until_element_is_clickable(self.sorting_container)
        dropdown.click()
        option = self._wait_until_element_is_clickable(locator)
        option.click()

    def sort_by_name_asc(self):
        self._select_sorting_option(self.name_asc_sorting)

    def sort_by_name_desc(self):
        self._select_sorting_option(self.name_desc_sorting)

    def sort_by_price_asc(self):
        self._select_sorting_option(self.price_asc_sorting)

    def sort_by_price_desc(self):
        self._select_sorting_option(self.price_desc_sorting)

