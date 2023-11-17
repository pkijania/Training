from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestPage:
    def __init__(self):
        self.driver = webdriver.Edge("D:\Programy\Selenium\Webdriver\msedgedriver.exe")
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def run(self):
        login = LoggingIn(self.driver)
        login.logging_in("standard_user", "secret_sauce")
        add = AddingProducts(self.driver)
        add.adding_products()
        validate = ValidatingPurchase(self.driver)
        validate.validating_purchase("John", "Smith", "54-254")
        logout = LoggingOut(self.driver)
        logout.logging_out()

class Locators:
        user_name = "user-name"
        password = "password"
        login_button = "login-button"
        add_to_cart_backpack = "add-to-cart-sauce-labs-backpack"
        add_to_cart_bike_light = "add-to-cart-sauce-labs-bike-light"
        button = "//span[text()='2']"
        checkout = "checkout"
        first_name = "firstName"
        last_name = "lastName"
        postal_code = "postalCode"
        continue_button = "continue"
        finish = "finish"
        back_to_products = "back-to-products"
        menu = "react-burger-menu-btn"
        logout = "Logout"

class LoggingIn:
    def __init__(self, driver):
        self.driver = driver

    def logging_in(self, standard_user, secret_sauce):
        self.driver.find_element(By.ID, Locators.user_name).send_keys(standard_user)
        self.driver.find_element(By.ID, Locators.password).send_keys(secret_sauce)
        self.driver.find_element(By.ID, Locators.login_button).click()

class AddingProducts:
    def __init__(self, driver):
        self.driver = driver

    def adding_products(self):
        self.driver.find_element(By.ID, Locators.add_to_cart_backpack).click()
        self.driver.find_element(By.ID, Locators.add_to_cart_bike_light).click()
        self.driver.find_element(By.XPATH, Locators.button).click()
        self.driver.find_element(By.NAME, Locators.checkout).click()
        
class ValidatingPurchase:
    def __init__(self, driver):
        self.driver = driver

    def validating_purchase(self, name, surname, pcode):
        self.driver.find_element(By.NAME, Locators.first_name).send_keys(name)
        self.driver.find_element(By.NAME, Locators.last_name).send_keys(surname)
        self.driver.find_element(By.NAME, Locators.postal_code).send_keys(pcode)
        self.driver.find_element(By.NAME, Locators.continue_button).click()
        self.driver.find_element(By.NAME, Locators.finish).click()
        self.driver.find_element(By.NAME, Locators.back_to_products).click()

class LoggingOut:
    def __init__(self, driver):
        self.driver = driver

    def logging_out(self):      
        self.driver.find_element(By.ID, Locators.menu).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.LINK_TEXT, Locators.logout).click()

test = TestPage()
test.run()