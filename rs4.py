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

        categories_expected = ['Home', 'Courses', 'All Access Plan', 'Learning Paths', 'Mentorship', 'Job Support', 'Practice', 'Blog', 'More']
        
        iframe = driver.find_element_by_xpath("//iframe[@id='courses-iframe']")
        driver.switch_to.frame(iframe)

        menu = driver.find_elements_by_xpath("/html/body/app-root/div/header/div[2]/div/div/div[2]/nav/div[2]/ul/li")

        categories = []

        for x in range(len(menu)):
            categories.append(menu[x].text)
        
        self.assertEqual(categories, categories_expected)

        print(categories)
 
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
