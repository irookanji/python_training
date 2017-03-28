# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time, unittest

from selenium.webdriver.support.wait import WebDriverWait

from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_address(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        # self.wd.implicitly_wait(60)

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def add_group(self, wd, group):
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "add new")))
        wd.find_element_by_link_text("add new").click()
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.NAME, "firstname")))
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group.name)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def test_test_address(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        self.login(wd, "admin", "secret")
        self.add_group(wd, Group(name="Vitas"))
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "home page")))
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
