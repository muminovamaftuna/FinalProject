# Тест: 1.8. Проверка добавления товара в корзину
# Объект тестирования: https://www.saucedemo.com/v1/
# Тип теста: Функциональный, позитивный

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_add_product_to_cart():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # --- Шаг 1: Открыть сайт и авторизоваться ---
    driver.get("https://www.saucedemo.com/v1/")
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    # Проверка успешного входа
    assert "inventory.html" in driver.current_url, "Не удалось войти"
    print("Авторизация прошла успешно")

    # --- Шаг 2: Добавить первый товар в корзину ---
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart_button.click()
    time.sleep(2)

    # --- Шаг 3: Перейти в корзину ---
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()
    time.sleep(2)

    # --- Шаг 4: Проверка товара в корзине ---
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) > 0, "Корзина пустая, товар не добавлен"

    # Проверка названия и цены первого товара
    product_name = cart_items[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    product_price = cart_items[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"🛒 В корзине товар: {product_name}, цена: {product_price}")

    driver.quit()
    print("Товар успешно добавлен в корзину")
