from misis_po_kabanova.pages.main_page import MainPage
from misis_po_kabanova.pages.Top100Page import Top100Page
from misis_po_kabanova.conftest import driver


class Test:

    # def test_get_notifications(self, driver):
    #     main_page = MainPage(driver, 'https://zvuk.com')
    #     main_page.open()
    #     # time.sleep(3000)
    #     main_page.close_greetings_if_exists()
    #     main_page.auth()
    #     # time.sleep(3000)
    #     main_page.open_notifications()
    #     all_links = main_page.get_list_of_notifications()
    #     print(all_links)

    def test_get_top_songs(self, driver):
        main_page = MainPage(driver, 'https://zvuk.com')
        main_page.open()
        main_page.close_greetings_if_exists()
        main_page.go_to_top100_page()
        top100_page = Top100Page(driver, 'https://zvuk.com/top100')
        top_songs_titles = top100_page.get_top_songs()
        print(top_songs_titles)

