import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
import time

class SuggessionClassExample(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '/Users/ripio/Documents/chromedriver')
        driver = self.driver
        driver.implicitly_wait(2)
    
    def test_suggession_class_example(self):
        driver = self.driver
        driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
        
        table = driver.find_elements_by_id('product')[1]
        rows = table.find_elements_by_tag_name("tr")
        rows_len = len(rows)

        total_amount = 0
        
        for i in range(rows_len):
            columns = rows[i].find_elements_by_tag_name("td")

            if(len(columns) == 4):
                total_amount = total_amount + int(columns[3].text)

        self.assertEqual(int(total_amount), 296)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
