import unittest
from selenium import webdriver

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/home/max/Dokumenty/chromedriver_linux64/chromedriver')

    def tearDown(self):
        self.driver.close()