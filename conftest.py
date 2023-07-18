import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Фикстура драйвера для запуска браузера
@pytest.fixture(scope="session")
def browser():
    try:
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        yield driver
    finally:
        # Закрываем браузер
        driver.quit()
