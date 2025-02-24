
import time

import pytest
from pages.product_page import AddToBasket
from pages.locators import ProductPageLocators

@pytest.mark.parametrize('link', [str(num) for num in range(0, 1)])

def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = AddToBasket(browser=browser, url=link)
    page.open()

    page.add_item_to_basket()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    time.sleep(1)

    page.price_in_basket_equal_price_item()
    page.title_in_basket_equal_title_item()