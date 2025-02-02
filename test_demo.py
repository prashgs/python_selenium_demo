import unittest
from selenium import webdriver


class TestUbuntuHomepage(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='selenium_drivers/geckodriver')

    def testTitle(self):
        self.browser.get('http://www.ubuntu.com/')
        self.assertIn('Ubuntu', self.browser.title)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
