# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest

from selenium.webdriver.support.wait import WebDriverWait

from group_1 import Group_1

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

    def fill_group_form(self, wd, group_1):
        wait = WebDriverWait(wd, 5)
        wait.until(EC.element_to_be_clickable((By.NAME, "firstname")))
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group_1.name)

    def test_address(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")
        # login
        self.login(wd, username="admin", password="secret")
        # open group page
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wait = WebDriverWait(wd, 5)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "add new")))
        # init group creation
        wd.find_element_by_link_text("add new").click()
        wait = WebDriverWait(wd, 5)
        wait.until(EC.element_to_be_clickable((By.NAME, "firstname")))
        # fill group form
        self.fill_group_form(wd, Group_1(name="Vitas"))
        # submit group creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # return to groups page
        wait = WebDriverWait(wd, 5)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "home page")))
        wd.find_element_by_link_text("home page").click()
        # logout
        wd.find_element_by_link_text("Logout").click()


    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
