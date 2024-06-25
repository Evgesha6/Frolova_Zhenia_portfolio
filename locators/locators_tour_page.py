import os

# import section

from page.base_page import WebPage
from page.elements import WebElement, ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://systemofadown.com/tour/'

        super().__init__(web_driver, url)

    btn_headers_home = WebElement(id='menu-item-11')
    btn_headers_tour = WebElement(id='menu-item-12')
    btn_headers_merch = WebElement(id='menu-item-13')
    btn_headers_music = WebElement(id='menu-item-14')

    btn_join_the_list = WebElement(xpath='//*[@title="Join The Mailing List"]')

    btn_home_link = WebElement(xpath='//*[contains(text(), "Home")]')
    btn_tour_link = WebElement(xpath='//*[contains(text(), "Tour")]')
    btn_merch_link = WebElement(xpath='//*[contains(text(), "Merch")]')
    btn_music_link = WebElement(xpath='//*[contains(text(), "Music")]')

    btn_footers_home = WebElement(xpath='(//footer//a)[1]')
    btn_footers_tour = WebElement(xpath='(//footer//a)[2]')
    btn_footers_merch = WebElement(xpath='(//footer//a)[3]')
    btn_footers_music = WebElement(xpath='(//footer//a)[4]')
