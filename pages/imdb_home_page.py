from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ImdbHomePage(BasePage):
    SEARCH_FIELD = (By.ID, "suggestion-search")
    SEARCH_BTN = (By.CLASS_NAME, "ipc-icon--magnify")

    def search_movie(self, movie_name):
        self.enter_text(self.SEARCH_FIELD, movie_name)
        self.click(self.SEARCH_BTN)