import allure
import pytest_check as check
from locators.locators_main_page import MainPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедера')
def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    locators = MainPage(web_browser)

    header_elements = [
        (locators.btn_headers_home, 'HOME'),
        (locators.btn_headers_tour, 'TOUR'),
        (locators.btn_headers_merch, 'MERCH'),
        (locators.btn_headers_music, 'MUSIC')
    ]

    for elements, elements_text in header_elements:
        check.is_true(elements.is_visible())
        check.is_true(elements.is_clickable())
        check.equal(elements.get_text(), elements_text)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки футера')
def test_footers(web_browser):
    """Этот тест проверяет футер главной страницы"""

    locators = MainPage(web_browser)

    footer_elements = [
        (locators.btn_footers_home, 'HOME'),
        (locators.btn_footers_tour, 'TOUR'),
        (locators.btn_footers_merch, 'MERCH'),
        (locators.btn_footers_music, 'MUSIC')
    ]

    for elements, elements_text in footer_elements:
        check.is_true(elements.is_visible())
        check.is_true(elements.is_clickable())
        check.equal(elements.get_text(), elements_text)
