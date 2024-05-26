import allure
import pytest_check as check
from locators.locators_main_page import MainPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедера')
def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    locators = MainPage(web_browser)

    header_elements = [
        # (locators.btn_headers_home, 'HOME'),
        # (locators.btn_headers_tour, 'TOUR'),
        # (locators.btn_headers_merch, 'MERCH'),
        (locators.btn_headers_music, 'MUSIC')
    ]

    for elements, elements_text in header_elements:
        check.is_true(elements.is_visible())
        check.is_true(elements.is_clickable())
        check.equal(elements.get_text(), elements_text)