from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ImdbMoviePage(BasePage):
    MOVIE_NAME = (By.CLASS_NAME, "sc-cb6a22b2-0")
    RATING = (By.CLASS_NAME, "sc-4dc495c1-1")

    def get_rating(self):
        return self.find_element(self.RATING).text     

    def get_Title(self):
        return self.find_element(self.MOVIE_NAME).text                                    