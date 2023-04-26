from selenium import webdriver
import pytest
from pages.google_homepage import GoogleHomepage


def test_google_homepage_title():
    # Launch the browser and navigate to the Google homepage
    driver = webdriver.Chrome()
    google_homepage = GoogleHomepage(driver)
    google_homepage.load()

    # Search for a keyword and verify that the page title contains the word "Google"
    google_homepage.search("test automation")
    assert google_homepage.is_title_matches()

    # Close the browser
    driver.quit()
