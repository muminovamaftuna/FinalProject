# Тест: 1.2. Проверка успешной авторизации с НЕ валидными данными
# Объект тестирования: https://www.saucedemo.com/v1/
# Тип теста: Функциональный, негативный
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_login_with_invalid_data(driver):

    driver.get("https://www.saucedemo.com/v1/index.html")

    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys("standard_user")
    password_field.send_keys("wrong_password")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
    ).text

    expected_message = "Epic sadface: Username and password do not match any user in this service"

    assert error_message == expected_message, (
        f"ОШИБКА! Ожидалось сообщение: '{expected_message}', но получили: '{error_message}'"
    )

    assert "inventory" not in driver.current_url, "Пользователь не должен попасть на страницу товаров"
