import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class SuggessionClassExample(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '/Users/ripio/Documents/chromedriver')
        driver = self.driver
        driver.implicitly_wait(5)
    
    def test_suggession_class_example(self):
        driver = self.driver
        driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
        
        suggession_class = driver.find_element_by_id('autocomplete')
        suggession_class.clear()
        suggession_class.send_keys('Vene')
        time.sleep(1)

        action = ActionChains(driver)
        suggession_class.send_keys(Keys.CONTROL,Keys.ARROW_DOWN)
        suggession_class.send_keys(Keys.CONTROL,Keys.ENTER)

        suggession_text = suggession_class.get_attribute('value')
 
        self.assertEqual(suggession_text,'Venezuela')
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
