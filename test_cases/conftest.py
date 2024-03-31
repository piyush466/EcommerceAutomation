from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/client/")
    driver.implicitly_wait(10)
    return driver
