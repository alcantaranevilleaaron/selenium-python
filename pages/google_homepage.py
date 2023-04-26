from selenium.webdriver.common.by import By
from utilities.retry_util import retry


class GoogleHomepage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com"
        self.search_box_name = "q"

    def navigate_to_homepage(self):
        self.driver.get(self.url)

    @retry
    def search_for(self, keyword):
        search_box = self.driver.find_element(By.NAME, self.search_box_name)
        search_box.send_keys(keyword)
        search_box.submit()

    def get_title(self):
        return self.driver.title

    def is_title_matches(self):
        return "Google" in self.driver.title
