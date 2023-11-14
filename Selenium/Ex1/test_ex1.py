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
        login.logging_in()
        add = AddingProducts(self.driver)
        add.adding_products()
        validate = ValidatingPurchase(self.driver)
        validate.validating_purchase()
        logout = LoggingOut(self.driver)
        logout.logging_out()

class LoggingIn:
    def __init__(self, driver):
        self.driver = driver

    def logging_in(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

class AddingProducts:
    def __init__(self, driver):
        self.driver = driver

    def adding_products(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        self.driver.find_element(By.XPATH, "//span[text()='2']").click()
        self.driver.find_element(By.NAME, "checkout").click()
        
class ValidatingPurchase:
    def __init__(self, driver):
        self.driver = driver

    def validating_purchase(self):
        self.driver.find_element(By.NAME, "firstName").send_keys("John")
        self.driver.find_element(By.NAME, "lastName").send_keys("Smith")
        self.driver.find_element(By.NAME, "postalCode").send_keys("54-254")
        self.driver.find_element(By.NAME, "continue").click()
        self.driver.find_element(By.NAME, "finish").click()
        self.driver.find_element(By.NAME, "back-to-products").click()

class LoggingOut:
    def __init__(self, driver):
        self.driver = driver

    def logging_out(self):      
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

test = TestPage()
test.run()