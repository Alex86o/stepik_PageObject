import pytest
from pages.product_page import AddToBasket
from pages.locators import ProductPageLocators


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = AddToBasket(browser=browser, url=link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.TITLE_IN_BASKET)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = AddToBasket(browser=browser, url=link)
    page.open()

    assert page.is_not_element_present(*ProductPageLocators.TITLE_IN_BASKET)


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = AddToBasket(browser=browser, url=link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    assert page.is_disappeared(*ProductPageLocators.TITLE_IN_BASKET)