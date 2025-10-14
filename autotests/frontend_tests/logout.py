# 1.3. Тест: Проверка выхода пользователя из системы
# Объект тестирования: https://www.saucedemo.com/v1/
# Тип теста: Функциональный, позитивный

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_logout():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/v1/index.html")
    time.sleep(2)

    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Вход выполнен")

    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
    time.sleep(2)

    # --- Открываем бургер-меню ---
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "bm-burger-button"))
    ).click()
    print("Меню открыто")

    # Добавляем паузу, чтобы меню успело открыться
    time.sleep(3)

    # --- Нажимаем Logout ---
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()
    print("Выход выполнен")

    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )
    assert driver.find_element(By.ID, "login-button").is_displayed()
    print("Вернулись на страницу входа")

    time.sleep(2)
    driver.quit()
