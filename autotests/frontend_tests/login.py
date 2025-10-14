# Тест: 1.1. Проверка успешной авторизации с валидными данными
# Объект тестирования: https://www.saucedemo.com/v1/
# Тип теста: Функциональный, позитивный

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_successful_login():
    # ChromeDriverManager сам скачивает нужную версию под Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()


    # --- Шаг 1: Перейти на страницу авторизации ---
    driver.get("https://www.saucedemo.com/v1/")

    # --- Шаг 2: Ввести логин и пароль ---
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")

    # --- Шаг 3: Нажать кнопку Login ---
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    time.sleep(2)  # пауза для того чтобы страница загрузилась

    # Проверка, перехода на страницу inventory.html
    assert "inventory.html" in driver.current_url, "Пользователь не попал на страницу товаров"

    # Проверка, наличие на странице заголовка Products
    page_title = driver.find_element(By.CLASS_NAME, "product_label").text
    assert page_title == "Products", " Заголовок 'Products' не найден"

    # Проверка, отображения товаровы
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0, "Список товаров не отображается"

    print("Тест пройден: Авторизация успешна, товары отображаются корректно")

    driver.quit()
