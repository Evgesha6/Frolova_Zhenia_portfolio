import allure
import pytest_check as check
from locators.locators_tour_page import MainPage


@allure.story('Тест для проверки страницы tour')
@allure.feature('Тест для проверки хедера')
def test_headers_tour(web_browser):
    """Этот тест проверяет хедер страницы tour"""

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


@allure.story('Тест для проверки страницы tour')
@allure.feature('Тест для проверки кнопки')
def test_headers_tour(web_browser):
    """Этот тест проверяет кнопкe страницы tour"""

    locators = MainPage(web_browser)

    btn_elements = (locators.btn_join_the_list, 'JOIN THE LIST'),

    for elements, elements_text in btn_elements:
        check.is_true(elements.is_visible())
        check.is_true(elements.is_clickable())
        check.equal(elements.get_text(), elements_text)


@allure.story('Тест для проверки страницы tour')
@allure.feature('Тест для проверки адреса ссылок')
def test_headers_link_tour(web_browser):
    """Этот тест проверяет адреса ссылок хедера страницы tour"""

    locators = MainPage(web_browser)

    link_header_elements = [
        (locators.btn_home_link, 'https://systemofadown.com/'),
        # (locators.btn_tour_link, 'https://systemofadown.com/tour/'),
        (locators.btn_merch_link, 'http://store.systemofadown.com/'),
        (locators.btn_music_link, 'https://systemofadown.com/albums')
    ]

    with allure.step('Проверка на кликабельность'):
        for elements, links in link_header_elements:
            check.is_true(elements.is_visible())
            check.is_true(elements.is_clickable())
            check.equal(elements.get_attribute('href'), links)


@allure.story('Тест для проверки страницы tour')
@allure.feature('Тест для проверки футера')
def test_footers_tour(web_browser):
    """Этот тест проверяет футер страницы tour"""

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
