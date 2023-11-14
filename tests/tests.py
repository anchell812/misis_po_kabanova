from misis_po_kabanova.pages.main_page import MainPage
from misis_po_kabanova.pages.Top100Page import Top100Page
from misis_po_kabanova.conftest import driver
import os
import datetime


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
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        folder_name = "reposts"
        folder_path = os.path.join(os.getcwd(), folder_name)
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, 'results.txt')
        with open(file_path, 'w') as file:
            for song in top_songs_titles:
                file.write(str(song) + '\n')
        return top_songs_titles

