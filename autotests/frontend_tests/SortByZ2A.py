# Тест: 1.7. Проверка успешной авторизации с валидными данными
# Объект тестирования: https://www.saucedemo.com/v1/
# Тип теста: Функциональный, позитивный
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_sort_by_name_z_to_a():
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
    sort_dropdown.select_by_value("za")
    time.sleep(3)


    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    names_list = [item.text for item in items]
    print("Названия товаров на странице:", names_list)


    assert names_list == sorted(names_list, reverse=True), "Ошибка сортировки"
    print("Товары отсортированы по названию от Z к A")

    driver.quit()
    print("Тест успешно завершен!")

