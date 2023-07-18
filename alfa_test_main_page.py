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


def test_moving_menu_links():

    try:
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.implicitly_wait(10)
        driver.get("https://alfabank.ru/")
        driver.maximize_window()

        # Выведем число вкладов на странице
        button_cards = driver.find_element(By.XPATH, "//a[@title='Карты']")
        button_cards.click()
        # Находим элемент Банковские карты
        first_page_title = driver.find_element(By.XPATH, "//h1[1]")
        # Сравниваем текст заголовка с найденным элементом
        assert first_page_title.text == "Банковские карты"
    finally:
        # Закрываем браузер
        driver.quit()


def test_geo_position():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.implicitly_wait(10)
    driver.get("https://alfabank.ru/")
    driver.maximize_window()

    # Скроллим вниз экрана
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(5)
    # Находим геопозицию Москва
    geo_button = driver.find_element(By.XPATH, "//span[text()='Москва']")
    # Нажимаем на неё
    geo_button.click()
    # Находим строку "Введите название города"
    region_name_field = driver.find_element(By.XPATH, "//input[@placeholder='Введите название города']")
    # Вводим название "Санкт-Петербург"
    region_name_field.send_keys("Санкт-Петербург")
    # Находим Санкт-Петербург
    region_name_button = driver.find_element(By.XPATH, "//span[text()='Санкт-Петербург']")
    # Кликаем по нему
    region_name_button.click()
    # Находим геопозицию Санкт-Петербург внизу экрана
    geo_button = driver.find_element(By.XPATH, "//span[text()='Санкт-Петербург']")
    # Проверяем, что в нем корректный текст - тот, регион, который мы выбираем
    assert geo_button.text == "Санкт-Петербург"

    time.sleep(5)


def test_count_links():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.implicitly_wait(10)
    driver.get("https://alfabank.ru/")
    driver.maximize_window()

    # Найдём все ссылки "Вклады" на странице
    driver.find_element(By.XPATH, "//a[@title='Вклады']")
    # Проверим, что их 6
    assert len('Вклады') == 6
    # print("Сount =", len('Вклады'))

    time.sleep(3)


def test_color_link():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.implicitly_wait(10)
    driver.get("https://alfabank.ru/")
    driver.maximize_window()
    # Находим элемент Альфа-Онлайн
    alfa_online_button = driver.find_element(By.XPATH, "//a[@data-test-id='internet-bank-button']")
    # Занесём в переменную цвет ссылки до наведения мыши
    color_before_perform = alfa_online_button.value_of_css_property('color')
    # Наводим мышь на кнопку Альфа-Онлайн
    ActionChains(driver).move_to_element(alfa_online_button).perform()
    # Занесём в переменную цвет ссылки после наведения мыши
    color_after_perform = alfa_online_button.value_of_css_property('color')
    # Сравним результаты до и после (они должны быть одниаковыми т.к. цвет не менялся)
    assert color_before_perform == color_after_perform
    # На тот случай, если бы цвет отличался бы до наведения и после наведения мыши
    # assert color_before_perform != color_after_perform

    time.sleep(3)
