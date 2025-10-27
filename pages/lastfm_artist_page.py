from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LastfmArtistPage(BasePage):
    LASTEST_RELEASE = (By.CLASS_NAME, "artist-header-featured-items-item-date")

    def get_lastest_release_date(self):
        return self.find_element(self.LASTEST_RELEASE).text                                    