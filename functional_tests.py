from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import unittest

class WebPageTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # You may need to change this.
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.browser = webdriver.Firefox(options=options)
        # You will need to update to my_page.html in your activity folder.
        self.browser.get('file:///c:/users/brand/dropbox/webprogramming/activities/activity_02/my_page.html')

    def tearDown(self):
        self.browser.quit()

    # Brandon has heard about a great new website that describes the latest
    # technological innovation: an automated robotic taco assembler.
    def test_web_page(self):

        # Brandon types in the address for the website. He notices that the 
        # title mentions the words "taco" and "robot".
        self.assertIn('taco', self.browser.title.lower())
        self.assertIn('robot', self.browser.title.lower())

        # He sees a heading on the main page that gives a brief description
        # of the product.
        header_text = self.browser.find_element(By.XPATH, "/html/body/header/h1").text.lower()
        self.assertIn('taco', header_text)
        self.assertIn('robot', header_text)
        self.assertIn('sentient', header_text)
        self.assertIn('obedient', header_text)

        # He sees a list of possible ingredients the robot can put on tacos.
        ingredient_list = self.browser.find_element(By.XPATH, "/html/body/section/article/ul")
        ingredients = ingredient_list.find_elements_by_tag_name("li")
        ingredient_text = [item.text for item in ingredients]
        self.assertIn('shell', ingredient_text)
        self.assertIn('meat', ingredient_text)
        self.assertIn('lettuce', ingredient_text)
        self.assertIn('cheese', ingredient_text)
        self.assertIn('guacamole', ingredient_text)
        self.assertIn('hot sauce', ingredient_text)
        self.assertIn('arsenic', ingredient_text)
        self.assertIn('sour cream', ingredient_text)

        # Looking back up, he sees a naviation bar with links to different
        # models of taco robots.
        nav_links = self.browser.find_elements(By.XPATH, "/html/body/nav/a")
        nav_link_text = [item.text for item in nav_links]
        self.assertIn('Soft TacoBot 3000', nav_link_text)
        self.assertIn('Hard TacoBot 3000', nav_link_text)
        self.assertIn('Gordita Crunch TacoBot 3000', nav_link_text)      
    
        # He reads a quote from a satisfied customer in a side panel.
        quote = self.browser.find_element(By.XPATH, "/html/body/section/aside/blockquote")
        self.assertIn('tacos are to die for', quote.text)
    
        # He notices financing options on a side panel
        financing = self.browser.find_element(By.XPATH, "/html/body/section/aside/p")
        self.assertIn('just 387 easy payments of $860', financing.text)
    
        # He finds a paragraph in tiny font on the footer of the page with
        # various legal disclaimers.
        footer = self.browser.find_element(By.XPATH, "/html/body/footer")
        self.assertIn('48 hour warranty for obedience', footer.text)
        self.assertIn('not responsible for the actions of the TacoBot 3000 after this time period', footer.text)
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')