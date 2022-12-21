import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestBlogcheckarticle():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_blogcheckarticle(self):
        self.driver.get("https://блог.новео.рф")
        self.driver.find_element(
            By.CSS_SELECTOR, ".post-list-unit:nth-child(10) .post-list-unit__title").click()
        assert self.driver.find_element(
            By.CSS_SELECTOR, ".single-post__title").text == "Валидация данных в Nest"
