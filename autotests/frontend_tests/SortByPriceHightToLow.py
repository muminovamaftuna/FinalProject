# Тест: 1.5. Проверка сортировки товаров по цене
# Объект тестирования: https://www.saucedemo.com/v1/
# Тип теста: Функциональный, позитивный
# Цель: Проверить корректность сортировки товаров от самой высокой цены к самой низкой

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_sort_by_price_high_to_low():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/v1/")
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)


    assert "inventory.html" in driver.current_url, "Ошибка: не удалось войти"
    print("Вход выполнен успешно")

    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value("hilo")
    time.sleep(3)


    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    price_list = [float(p.text.replace("$", "")) for p in prices]
    print("Цены на странице после сортировки:", price_list)

    assert price_list == sorted(price_list, reverse=True), "Ошибка сортировки"
    print("Товары отсортированы от высокой цены к низкой")

    driver.quit()
    print("Мафтуна молодец))")

