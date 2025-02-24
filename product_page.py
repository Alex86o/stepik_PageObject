
from .main_page import MainPage
from .locators import ProductPageLocators


class AddToBasket(MainPage):
    def add_item_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET).click()

    def price_in_basket_equal_price_item(self):
        price1 = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        price2 = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price1 == price2, "Price basket not equal price product"

    def title_in_basket_equal_title_item(self):
        title1 = self.browser.find_element(*ProductPageLocators.TITLE_BASKET).text
        title2 = self.browser.find_element(*ProductPageLocators.TITLE_PRODUCT).text
        assert title1 == title2, "Price basket not equal price product"