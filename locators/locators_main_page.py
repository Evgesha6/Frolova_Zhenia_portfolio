import os

from page.base_page import WebPage
from page.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://systemofadown.com/'

        super().__init__(web_driver, url)

    # btn_headers_home = WebElement(ID='//div[@id="menu-item-14"]//href[contains(text(),"Music")]')
    # btn_headers_tour = WebElement(ID='menu-item-12,"TOUR"')
    # btn_headers_merch = WebElement(ID='menu-item-13,"MERCH"')
    btn_headers_music = WebElement(xpath='//div[@id="menu-item-14"]//a[contains(@href,"Music")]')
