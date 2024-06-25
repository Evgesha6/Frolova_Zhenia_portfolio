from lib2to3.pgen2 import driver

import allure
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
from locators.locators_join_list import MainPage


@allure.story('Тест для проверки страницы предзаписи')
@allure.feature('Тест для проверки полей')
def test_input(web_browser):
    """Этот тест проверяет поля страницы предзаписи"""

    locators = MainPage(web_browser)

    header_elements = [
        locators.input_first_name,
        locators.input_email,
        locators.input_b_day_date,
        locators.input_b_day_month,
        locators.btn_enter
    ]

    for elements in header_elements:
        check.is_true(elements.is_visible())
        check.is_true(elements.is_clickable())


@allure.story('Тест для проверки страницы предзаписи')
@allure.feature('Тест для проверки заполнения полей')
def test_input(web_browser):
    """Этот тест проверяет заполнениеп полей страницы предзаписи"""

    locators = MainPage(web_browser)

    FIRST_NAME = 'Evgeniya'
    USER_EMAIL = 'test@gmail.com'


    with allure.step('Проверка на ввод текста и проверка результата'):
        name = FIRST_NAME
        email=USER_EMAIL

    locators.input_first_name.send_keys(name)
    locators.input_email.send_keys(email)
    # locators.input_b_day_date.click(2)
    # locators.btn_16.is_selected()
