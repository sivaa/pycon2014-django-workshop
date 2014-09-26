from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import time

class EndUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def add_content_in_movie_name_input_box(self, content):
        input_box = self.browser.find_element_by_id("id_movie_name")
        input_box.send_keys(content)
        input_box.send_keys(Keys.ENTER)

    def check_content_in_movie_list_table(self, content):
        table = self.browser.find_element_by_id("id_movie_list_table")
        rows = table.find_elements_by_tag_name("tr")
        time.sleep(2)
        self.assertTrue(any(content in row.text for row in rows),
                        "Movie %s is not added to the table. Table content: %s" % (content, table.text))


    def test_add_a_movie_and_fetch_it(self):
        self.browser.get("localhost:8000")

        # Check the title
        self.assertIn("Movie", self.browser.title)
		
        time.sleep(5)
		
        # Check the heading
        heading = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Movie", heading)

        time.sleep(5)
		
        # Check the input text box
        input_box = self.browser.find_element_by_id("id_movie_name")
        input_box_place_holder = input_box.get_attribute("placeholder")
        self.assertEqual(input_box_place_holder, "Enter a Movie Name")

        time.sleep(5)
		
        # Add a movie name in that text box
        self.add_content_in_movie_name_input_box("Troy")
        # Check that movie name in the list table
        self.check_content_in_movie_list_table("Troy")

        time.sleep(5)
		
        # Add one more movie name and Check that movie name in the list table
        self.add_content_in_movie_name_input_box("Terminator")
        self.check_content_in_movie_list_table("Terminator")

        time.sleep(5)
        #self.fail("Finish the Test")



if __name__ == '__main__':
    unittest.main()