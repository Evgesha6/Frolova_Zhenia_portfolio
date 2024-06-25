import os

# import section

from page.base_page import WebPage
from page.elements import WebElement, ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://store.systemofadown.com/'

        super().__init__(web_driver, url)

    btn_headers_home = WebElement(xpath='(//*[@aria-current="page"])[2]//span')
    btn_headers_apparel = WebElement(xpath='(//header//span)[9]')
    btn_headers_accessories = WebElement(xpath='(//header//span)[10]')
    btn_headers_music = WebElement(xpath='(//header//span)[11]')
    btn_headers_collections = WebElement(xpath='(//header//span)[12]')

    btn_search_merch = WebElement(xpath='//*[@aria-haspopup="dialog"]//span')
    btn_input = WebElement(id='Search-In-Modal')
    btn_search= WebElement(xpath='(//*[@aria-label="Search"])[3]')
    text_zone= WebElement(xpath='//*[@aria-labelledby="predictive-search-products"]//button')

    btn_country=WebElement(xpath='//*[@aria-controls="FooterCountryList"]')

    btn_headers_apparel1 = WebElement(xpath='(//header//summary)[5]')
    btn_count_apparel = ManyWebElements(xpath='(//*[@role="list"])[7]/li')
    btn_headers_accessories1 = WebElement(xpath='(//header//summary)[6]')
    btn_count_accessories = ManyWebElements(xpath='(//*[@role="list"])[8]/li')
    btn_headers_collections1 = WebElement(xpath='(//header//summary)[7]')
    btn_count_collections = ManyWebElements(xpath='(//*[@role="list"])[9]/li')