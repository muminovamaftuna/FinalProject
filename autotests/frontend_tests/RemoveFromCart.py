# 1.9 Тест: Добавление и удаление товара в корзине
# Объект тестирования: https://www.saucedemo.com/v1/
# Тип теста: Функциональный, позитивный

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_add_and_remove_product():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # --- Авторизация ---
    driver.get("https://www.saucedemo.com/v1/")
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    assert "inventory.html" in driver.current_url, "Не удалось войти"
    print("Вход выполнен успешно")

    # --- Добавление первого товара в корзину ---
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    print("Товар добавлен в корзину")
    time.sleep(2)

    # --- Переход в корзину ---
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    # --- Удаление товара ---
    driver.find_element(By.CLASS_NAME, "cart_button").click()
    print("Товар удалён из корзины")
    time.sleep(2)

    # --- Проверка, что корзина пустая ---
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 0, "Корзина не пустая после удаления товара"
    print("Корзина пустая, тест пройден")

    driver.quit()
