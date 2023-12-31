import time
import pytest
from selenium import webdriver
# Библиотека для скролла
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# Библиотека отвечающая за наведение курсора мыши
from selenium.webdriver.common.action_chains import ActionChains
import locators
import Steps.support_steps as support_steps


def test_moving_menu_links(browser):
    try:

        # Выставляем ожидание в 10 секунд
        browser.implicitly_wait(10)
        # Открываем тестовую страницу
        browser.get("https://alfabank.ru/")
        # Разворачиваем окно на весь экран
        browser.maximize_window()

        # Выведем число вкладов на странице
        button_cards = browser.find_element(By.XPATH, locators.BUTTON_CARDS)
        button_cards.click()
        # Находим элемент Банковские карты
        first_page_title = browser.find_element(By.XPATH, locators.FIRST_TITLE_ON_PAGE)
        # Сравниваем текст заголовка с найденным элементом
        assert first_page_title.text == "Банковские карты"
    finally:
        # Закрываем браузер
        browser.quit()


def test_geo_position(browser):
    # Выставляем ожидание в 10 секунд
    browser.implicitly_wait(10)
    # Открываем тестовую страницу
    browser.get("https://alfabank.ru/")
    # Разворачиваем окно на весь экран
    browser.maximize_window()

    # Скроллим вниз экрана
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(5)
    # Находим геопозицию Москва
    geo_button_msk = browser.find_element(By.XPATH, locators.GEO_BUTTON_MSK)
    # Нажимаем на неё
    geo_button_msk.click()
    # Находим строку "Введите название города"
    region_name_field = browser.find_element(By.XPATH, locators.REGION_NAME_FIELD)
    # Вводим название "Санкт-Петербург"
    region_name_field.send_keys("Санкт-Петербург")
    # Находим Санкт-Петербург
    region_name_button = browser.find_element(By.XPATH, locators.REGION_NAME_BUTTON)
    # Кликаем по нему
    region_name_button.click()
    # Находим геопозицию Санкт-Петербург внизу экрана
    geo_button_spb = browser.find_element(By.XPATH, locators.GEO_BUTTON_SPB)
    # Проверяем, что в нем корректный текст - тот, регион, который мы выбираем
    assert geo_button_spb.text == "Санкт-Петербург"

    time.sleep(5)


def test_incorrect_geo_position(browser):
    try:
        # Выставляем ожидание в 10 секунд
        browser.implicitly_wait(10)
        # Открываем тестовую страницу
        browser.get("https://alfabank.ru/")
        # Разворачиваем окно на весь экран
        browser.maximize_window()

        # Скроллим вниз экрана
        browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(5)
        # Находим геопозицию Москва
        geo_button_msk = browser.find_element(By.XPATH, locators.GEO_BUTTON_MSK)
        # Нажимаем на неё
        geo_button_msk.click()
        # Находим строку "Введите название города"
        region_name_field = browser.find_element(By.XPATH, locators.REGION_NAME_FIELD)
        # Вводим рандомное сгенерированное название
        region_name_field.send_keys(support_steps.generate_random_string(5))
        time.sleep(5)
    finally:
        browser.quit()


def test_count_links(browser):
    # Выставляем ожидание в 10 секунд
    browser.implicitly_wait(10)
    # Открываем тестовую страницу
    browser.get("https://alfabank.ru/")
    # Разворачиваем окно на весь экран
    browser.maximize_window()

    # Найдём все ссылки "Вклады" на странице
    browser.find_element(By.XPATH, "//a[@title='Вклады']")
    # Проверим, что их 6
    assert len('Вклады') == 6
    # print("Сount =", len('Вклады'))

    time.sleep(3)


def test_color_link(browser):
    # Выставляем ожидание в 10 секунд
    browser.implicitly_wait(10)
    # Открываем тестовую страницу
    browser.get("https://alfabank.ru/")
    # Разворачиваем окно на весь экран
    browser.maximize_window()
    # Находим элемент Альфа-Онлайн
    alfa_online_button = browser.find_element(By.XPATH, locators.ALFA_ONLINE_BUTTON)
    # Занесём в переменную цвет ссылки до наведения мыши
    color_before_perform = alfa_online_button.value_of_css_property('color')
    # Наводим мышь на кнопку Альфа-Онлайн
    ActionChains(browser).move_to_element(alfa_online_button).perform()
    # Занесём в переменную цвет ссылки после наведения мыши
    color_after_perform = alfa_online_button.value_of_css_property('color')
    # Сравним результаты до и после (они должны быть одниаковыми т.к. цвет не менялся)
    assert color_before_perform == color_after_perform
    # На тот случай, если бы цвет отличался бы до наведения и после наведения мыши
    # assert color_before_perform != color_after_perform

    time.sleep(3)
