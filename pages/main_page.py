import time
from misis_po_kabanova.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def close_greetings_if_exists(self):
        greeting_close_btns = self.driver.find_elements(By.XPATH, '//button[contains(@class, "MeetGreet_closeButton")]')
        if len(greeting_close_btns) > 0:
            greeting_close_btns[0].click()

    def auth(self):
        self.el_is_visible('//button[@aria-label="authenticate"]//div//p[text()="Войти"]')
        login_btn = self.driver.find_element(By.XPATH, '//button[@aria-label="authenticate"]//div//p[text()="Войти"]')
        login_btn.click()
        iframe = self.driver.find_element(By.XPATH, '//iframe[@title="ZvukIdModal"]')
        self.driver.switch_to.frame(iframe)
        self.el_is_visible('//div[contains(@class,"Phone")]/button[contains(@class,"Button")]')
        options_list = self.driver.find_element(By.XPATH, '//div[contains(@class,"Phone")]/button[contains(@class,"Button")]')
        options_list.click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        other_login = self.driver.find_element(By.XPATH, '//a[contains(text(),"альтернативный способ")]')
        other_login.click()
        login_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Email"]')
        login_input.click()
        login_input.send_keys('anchell@yandex.ru')
        pass_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Пароль"]')
        pass_input.send_keys("password")
        self.el_is_visible('//button[contains(@class, "loginButton")]')
        submit_btn = self.driver.find_element(By.XPATH, '//button[contains(@class, "loginButton")]')
        submit_btn.click()

    def open_notifications(self):
        self.el_is_visible('//button[@aria-label="notifications"]/span')
        notification_btn = self.driver.find_element(By.XPATH, '//button[@aria-label="notifications"]/span')
        notification_btn.click()
        # //div[contains(@class, "dotVisible")]

    def get_list_of_notifications(self):
        all_notifications = self.driver.find_elements(By.XPATH, '//div[contains(@class, "listItem")]//a')
        link_to_notification_item = [notification.get_attribute('href') for notification in all_notifications]
        return set(link_to_notification_item)

    def go_to_top100_page(self):
        top100_link = self.driver.find_element(By.XPATH, '//a/span[text()="Топ-100"]')
        top100_link.click()



