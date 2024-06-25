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
@allure.feature('Тест для проверки кнопок')
def test_headers(web_browser):
    """Этот тест проверяет кнопки главной страницы"""

    locators = MainPage(web_browser)

    btn_elements = [
        (locators.btn_shop_now, 'SHOP NOW'),
        (locators.btn_join_the_list, 'JOIN THE LIST'),
    ]

    for elements, elements_text in btn_elements:
        check.is_true(elements.is_visible())
        check.is_true(elements.is_clickable())
        check.equal(elements.get_text(), elements_text)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки адреса ссылок')
def test_headers_link(web_browser):
    """Этот тест проверяет адреса ссылок хедера главной страницы"""

    locators = MainPage(web_browser)

    link_header_elements = [
        (locators.btn_home_link, 'https://systemofadown.com/'),
        (locators.btn_tour_link, 'https://systemofadown.com/tour/'),
        (locators.btn_merch_link, 'http://store.systemofadown.com/'),
        (locators.btn_music_link, 'https://systemofadown.com/albums')
    ]

    with allure.step('Проверка на кликабельность'):
        for elements, links in link_header_elements:
            check.is_true(elements.is_visible())
            check.is_true(elements.is_clickable())
            check.equal(elements.get_attribute('href'), links)


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


# @allure.story('Тест для проверки главной страницы')
# @allure.feature('Тест для проверки нажатия кнопки')
# def test_click(web_browser):
#     """Этот тест проверяет нажатие кнопки"""
#
#    locators = MainPage(web_browser)
#
#    clickable_buttons = [
#        (locators.btn_join_the_list),
#        (locators.btn_shop_now)
#    ]
# # Нахождение элементов на странице
# single_click_btn = driver.find_element_by_id("singleClickBtn")
# # Нажатие на кнопки
# single_click_btn.click()
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dynamicClickMessage")))


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки количества плиток в блоке "SOAD MERCH"')
def test_count_box_main(web_browser):
    """Этот тест проверяет количество плиток в блоке "SOAD MERCH" """

    locators = MainPage(web_browser)

    with allure.step('Проверка количетва плиток'):
        count = locators.btn_count_box
        number = 4

        for count_elements in count:
            count_elements.click()
            check.equal(locators.btn_count_box.count(), number)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки количества плиток в блоке "SOAD MERCH"')
def test_count_video(web_browser):
    """Этот тест проверяет количество видео на главной странице """

    locators = MainPage(web_browser)

    with allure.step('Проверка количетва видео'):
        count = locators.video_count
        number = 2

        for count_elemnts in count:
            count_elemnts.click()
            check.equal(locators.video_count.count(), number)
