from pages.top_bar_menu import TopBarMenu
from pages.cart_products_page import CartProductsPage
from pages.checkout_page import CheckoutPage
from pages.checkout_fill_form_page import CheckoutFillFormPage
import pytest 


def test_successful_purchase_flow(standard_user_login_to_products_page):
    products_page = standard_user_login_to_products_page

    assert products_page.browser.current_url.endswith("/inventory.html")
    assert products_page.products_list_is_displayed()
    product_name = "Sauce Labs Backpack"
    product = products_page.find_product_by_name(product_name)
    assert product is not None, f"Product '{product_name}' not found on the Products page"
    product_price = product.get_product_price()
    assert products_page.count_products() == 6
    product.click_add_to_cart_button()

    cart_icon = TopBarMenu(products_page.browser)
    assert "1" == cart_icon.get_product_quantity()
    cart_icon.click_icon()

    cart = CartProductsPage(products_page.browser)
    product_in_cart = cart.find_product_by_name(product_name)
    assert product_in_cart is not None, f"Product '{product_name}' not found in cart"
    assert "1" == product_in_cart.get_item_quantity()
    assert product_price == product_in_cart.get_price()
    cart.click_checkout()

    fill_form_page = CheckoutFillFormPage(products_page.browser)
    fill_form_page.fill_checkout_form("Dor", "Fin", "01-0101")
    fill_form_page.click_continue()
    checkout = CheckoutPage(products_page.browser)
    assert products_page.browser.current_url.endswith("checkout-step-two.html")
    assert product_name == checkout.get_product_name()
    assert product_price == checkout.get_product_price()
    total_subprice = checkout.get_subtotal_price()
    assert product_price == total_subprice
   
    checkout.click_finish()
    assert checkout.completed_order_notification_is_displayed()

    


@pytest.mark.parametrize("first_name, last_name, postal_code, error_msg",
                        [
                        ("", "LastName", "12-434", "Error: First Name is required"),
                        ("FirstName", "", "12-432", "Error: Last Name is required"),
                        ("FirstName", "LastName", "", "Error: Postal Code is required")
                        ])
# --- Test validation of checkout information form ---
def test_checkout_form_validation(standard_user_login_to_products_page, first_name, last_name, postal_code, error_msg):
    products_page = standard_user_login_to_products_page
    assert products_page.products_list_is_displayed()
    first_product = products_page.find_products()[0]
    first_product.click_add_to_cart_button()
   
    top_bar = TopBarMenu(products_page.browser)
    top_bar.click_icon()

    cart_product_page = CartProductsPage(products_page.browser)
    cart_product_page.click_checkout()

    info_form = CheckoutFillFormPage(products_page.browser)
    info_form.fill_checkout_form(first_name, last_name, postal_code)
    info_form.click_continue()
    assert error_msg == info_form.get_error_message()


# ------ Products page: test sorting  ------
def test_sort_by_name_asc(standard_user_login_to_products_page):
    products_page = standard_user_login_to_products_page
    products_page.sort_by_name_asc()
    products = products_page.find_products()
    names = [p.get_product_name() for p in products]
    assert names == sorted(names), "Products are not sorted ascending by name"

def test_sort_by_name_desc(standard_user_login_to_products_page):
    products_page = standard_user_login_to_products_page
    products_page.sort_by_name_desc()
    products = products_page.find_products()
    names = [p.get_product_name() for p in products]
    assert names == sorted(names, reverse=True), "Products are not sorted descending by name"

def test_sort_by_price_asc(standard_user_login_to_products_page):
    products_page = standard_user_login_to_products_page
    products_page.sort_by_price_asc()
    products = products_page.find_products()
    prices = [p.get_product_price() for p in products]
    assert prices == sorted(prices), "Products are not sorted ascending by price (low to high)"

def test_sort_by_price_desc(standard_user_login_to_products_page):
    products_page = standard_user_login_to_products_page
    products_page.sort_by_price_desc()
    products = products_page.find_products()
    prices = [p.get_product_price() for p in products]
    assert prices == sorted(prices, reverse=True), "Products are not sorted descending by price (high to low)"






