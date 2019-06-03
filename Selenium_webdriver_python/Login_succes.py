# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome(executable_path=r'/home/max/Dokumenty/chromedriver_linux64/chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://executeautomation.com/demosite/Login.html")
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_name("UserName").click()
        driver.find_element_by_name("UserName").clear()
        driver.find_element_by_name("UserName").send_keys("testowy")
        driver.find_element_by_name("Password").clear()
        driver.find_element_by_name("Password").send_keys("testowy")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Login'])[2]/following::input[3]").click()
        self.accept_next_alert = True
        driver.find_element_by_name("generate").click()
        self.assertEqual("You generated a Javascript alert", self.close_alert_and_get_its_text())
        self.assertEqual("You pressed OK!", self.close_alert_and_get_its_text())

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
