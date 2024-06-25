import allure
import pytest_check as check

import locators
from locators.locators_merch_page import MainPage


@allure.story('Тест для проверки страницы магазина')
@allure.feature('Тест для проверки хедера')
def test_headers_store(web_browser):
    """Этот тест проверяет хедер страницы магазина"""

    locators = MainPage(web_browser)

    header_elements = [
        (locators.btn_headers_home, 'HOME'),
        (locators.btn_headers_apparel, 'APPAREL'),
        (locators.btn_headers_accessories, 'ACCESSORIES'),
        (locators.btn_headers_music, 'MUSIC'),
        (locators.btn_headers_collections, 'COLLECTIONS')
    ]

    for elements, elements_text in header_elements:
        check.is_true(elements.is_visible())
        check.is_true(elements.is_clickable())
        check.equal(elements.get_text(), elements_text)


@allure.story('Тест для проверки страницы магазина')
@allure.feature('Тест для проверки работоспособности инпута')
def test_input_store(web_browser):
    """Этот тест проверяет работоспособность инпута"""

    locators = MainPage(web_browser)

    locators.btn_search_merch.click()

    with allure.step('Проверка на кликабельность'):
        check.is_true(locators.btn_input.is_visible())

    with allure.step('Проверка на отображение'):
        check.is_true(locators.btn_input.is_clickable())

    with allure.step('Проверка плейсхолдера'):
        check.equal(locators.btn_input.get_attribute('placeholder'), 'Search')

    with allure.step('Проверка на ввод текст и роверка результата'):
        text_awake = 'awake'

        locators.btn_input.send_keys(text_awake)
        locators.btn_search.click(1)


@allure.story('Тест для проверки страницы магазина')
@allure.feature('Тест для проверки количества элементов в выпадающем списке')
def test_headers(web_browser):
    """Этот тест проверяет количество элементов в выпадающем списке"""

    locators = MainPage(web_browser)

    drop_down_btn = [(locators.btn_headers_apparel1, locators.btn_count_apparel, 5),
                     (locators.btn_headers_accessories1, locators.btn_count_accessories, 2),
                     (locators.btn_headers_collections1, locators.btn_count_collections, 6)]

    for btn, list, num in drop_down_btn:
        btn.click()

        with allure.step('Проверка количества плиток'):
            a = list.count()
            check.equal(a, num)
