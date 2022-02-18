import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class SuggessionClassExample(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '/Users/ripio/Documents/chromedriver')
        driver = self.driver
        driver.implicitly_wait(2)
    
    def test_suggession_class_example(self):
        driver = self.driver
        driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
        
        table = driver.find_element_by_id('product')

        rows = table.find_elements_by_tag_name("tr")
        rows_len = len(rows)
        
        for i in range(rows_len):
            columns = rows[i].find_elements_by_tag_name("td")
            if(len(columns) == 3):
                instructor = columns[0].text
                course = columns[1].text
                price = columns[2].text
                if(int(price) > 30):
                    print(f"Instructor:{instructor}\nCurso:{course}\nPrecio:{price}\n")

 
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
