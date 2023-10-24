from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
def test_selenium():
    import os
    run_env = os.getenv('RUN_ENV')
    print(run_env)

    options = EdgeOptions()
    options.use_chromium = True
    if run_env == 'ci':
        options.add_argument("--headless")
        options.add_argument("disable-gpu")

    driver = webdriver.Chrome(
        executable_path="D:\Programy\Selenium\Webdriver\msedgedriver.exe", options=options)

    #driver = Edge(executable_path="D:\Programy\Selenium\Webdriver\msedgedriver.exe", capabilities=edge_options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    #logging in
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    #adding products to a cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.XPATH, "//span[text()='2']").click()
    driver.find_element(By.NAME, "checkout").click()

    #typing personal data
    driver.find_element(By.NAME, "firstName").send_keys("John")
    driver.find_element(By.NAME, "lastName").send_keys("Smith")
    driver.find_element(By.NAME, "postalCode").send_keys("54-254")

    #validating the purchase
    driver.find_element(By.NAME, "continue").click()
    driver.find_element(By.NAME, "finish").click()

    #logging out
    driver.find_element(By.NAME, "back-to-products").click()
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.implicitly_wait(3)
    driver.find_element(By.LINK_TEXT, "Logout").click()

    #while True:
    #    pass