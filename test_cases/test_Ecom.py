import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjectModule.Ecommerce import New_Ecommerce
from Utilities.logging import LogGen

class TestEcomerces:
    log = LogGen().loggenerate()
    username1 = "piyushdravyakar48@gmail.com"
    password1 = "Piyush@123"

    def test_login(self,setup):
        self.log.info("*************Execution started**********")
        self.driver = setup
        self.log.info("*************Invoke the Browser**********")
        self.lg = New_Ecommerce(self.driver)
        self.lg.username(self.username1)
        self.log.info("your username is: %s", self.username1)
        self.lg.password(self.password1)
        self.log.info("your password1 is: %s", self.password1)
        self.lg.login()
        self.title = self.driver.title
        assert self.title == "Let's Shop"
        time.sleep(4)
        self.compare = self.driver.find_element(By.XPATH, self.lg.al_comparing_xpath).text
        print(self.compare)
        assert self.compare == "AUTOMATION"
        self.log.info("comapring the After login Text is match or not %s ",self.compare)
        self.driver.save_screenshot("C:\\Users\\ASUS\\PycharmProjects\\Ecommerce\\Screenshots\\piyush.png")
        self.log.info("*************Execution Done**********")
        print("Good")
