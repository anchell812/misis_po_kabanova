from misis_po_kabanova.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Top100Page(BasePage):

    def get_top_songs(self):
        top_links = self.driver.find_elements(By.XPATH, '//p[@itemprop="name"]//a')
        top_titles = [title.get_attribute('title') for title in top_links]
        return set(top_titles)

