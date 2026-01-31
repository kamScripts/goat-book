import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_todo_list(self):
        #Edith has heard about a cool new online t-do app.
        #She goes to check out its hompage
        self.browser.get('http://localhost:8000')

        #She notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)

        #She is invited to enter a to-do item staright away
        self.fail('Complete the test')

if __name__ == '__main__':
    unittest.main()