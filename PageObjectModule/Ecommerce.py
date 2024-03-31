from selenium import webdriver
from selenium.webdriver.common.by import By
# from Utilities.logging import LogGen

class New_Ecommerce:
    username_Id = "userEmail"
    password_Id = "userPassword"
    login_btn_Id = "login"
    al_comparing_xpath= "//h3"


    def __init__(self,driver):
        self.driver = driver

    def username(self,username):
        self.driver.find_element(By.ID, self.username_Id).send_keys(username)

    def password(self,password):
        self.driver.find_element(By.ID, self.password_Id).send_keys(password)

    def login(self):
        self.driver.find_element(By.ID, self.login_btn_Id).click()

