from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[name='login-password']")

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTRATION_REPEAT = (By.CSS_SELECTOR, "[name='registration-password2']")

class ProductPageLocators():
    BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    TITLE_BASKET = (By.CSS_SELECTOR, ".alertinner > strong" )
    TITLE_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
