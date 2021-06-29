from selenium import webdriver
import unittest
import HtmlTestRunner
import time
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage

class SauceDemo_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Safari() #driver for using safari
        #cls.driver = webdriver.chrome("../drivers/chromedriver") #chrome driver for using mac M1
        #cls.driver = webdriver.chrome("../drivers/chromedriver.exe") #chrome driver for using windows
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://www.saucedemo.com/")
        login = LoginPage(cls.driver)
        login.enter_username("standard_user")
        time.sleep(2)
        login.enter_password("secret_sauce")
        login.click_login()
        time.sleep(5)

    def test_add_to_cart(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.detail_product()
        homepage.add_to_cart()
        homepage.shopping_cart()
        quantity = homepage.cart_quantity()
        assert quantity == "1"

    def test_checkout_overview(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.checkout_button()
        homepage.first_name("Secret")
        time.sleep(3)
        homepage.last_name("Name")
        time.sleep(2)
        homepage.postal_code("12345")
        homepage.click_continue()
        product_name = homepage.checkout_overview()
        assert product_name == "Sauce Labs Backpack"

    def test_finish(self):
       driver = self.driver
       homepage = HomePage(driver)
       homepage.finish_checkout()
       complete = homepage.complete_checkout()
       assert complete == "THANK YOU FOR YOUR ORDER"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Finish")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Results'))