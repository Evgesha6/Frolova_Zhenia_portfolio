import os

# import section

from page.base_page import WebPage
from page.elements import WebElement, ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://wct.live/app/31160/system-of-a-down'

        super().__init__(web_driver, url)

    input_first_name = WebElement(xpath='//*[@name="first_name"]')
    input_email = WebElement(xpath='//input[@name = "email"]')
    input_b_day_date = WebElement(xpath='//*[@name="dobDay"]')
    input_b_day_month = WebElement(xpath='//*[@name="dobMonth"]')
    input_country = WebElement(xpath='//*[@name="country"]')
    btn_enter =WebElement(xpath='//*[@data-button-text="Enter"]')
    btn_16 = WebElement(xpath='//*[@name="dobDay"]/*[17]')