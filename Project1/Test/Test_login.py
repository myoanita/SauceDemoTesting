from selenium import webdriver
import unittest
import HtmlTestRunner
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage

class SauceDemo_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Safari() #driver for using safari
        #cls.driver = webdriver.Chrome("../drivers/chromedriver") #chrome driver for using mac M1
        #cls.driver = webdriver.Chrome("../drivers/chromedriver.exe") #chrome driver for using windows
        cls.driver = webdriver.Chrome("drivers/chromedriver_linux") # chrome driver for using linux
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_without_username_and_password(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        login = LoginPage(driver)
        login.click_login()
        error_message = login.error_message()
        assert error_message == "Epic sadface: Username is required"

    def test_login_without_username(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        login = LoginPage(driver)
        login.enter_password("secret_sauce")
        login.click_login()
        error_message = login.error_message()
        assert error_message == "Epic sadface: Username is required"

    def test_login_without_password(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.click_login()
        error_message = login.error_message()
        assert error_message == "Epic sadface: Password is required"

    def test_login_with_username_and_password_that_didnt_registered(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        login = LoginPage(driver)
        login.enter_username("testing")
        login.enter_password("testing")
        login.click_login()
        error_message = login.error_message()
        assert error_message == "Epic sadface: Username and password do not match any user in this service"

    def test_login_with_username_and_wrong_password(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("testing")
        login.click_login()
        error_message = login.error_message()
        assert error_message == "Epic sadface: Username and password do not match any user in this service"

    def test_login_with_username_and_password(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        login = LoginPage(driver)
        homepage = HomePage(driver)
        login.enter_username("standard_user")
        time.sleep(3)
        login.enter_password("secret_sauce")
        login.click_login()
        title = homepage.title_homepage()
        assert title == "PRODUCTS"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Finish")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Results'))

