import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# Тест успешной авторизации
@allure.title("Авторизация с валидными данными")
@allure.description("Проверяет, что пользователь может войти в систему с правильным логином и паролем.")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success(driver):
    with allure.step("Открыть страницу входа"):
        driver.get("https://www.saucedemo.com/v1/")
        allure.attach(driver.current_url, name="URL страницы входа", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Ввести корректные данные и нажать Login"):
        username_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")

        password_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("secret_sauce")

        login_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()

    with allure.step("Проверить, что вход выполнен успешно"):
        WebDriverWait(driver, 15).until(EC.url_contains("inventory.html"))
        assert "inventory.html" in driver.current_url, "Ошибка: не удалось войти"
        allure.attach(driver.current_url, name="URL после входа", attachment_type=allure.attachment_type.TEXT)
    print("Авторизация прошла успешно!")

#  Тест сортировки товаров по названию (Z → A)
@allure.title("Сортировка товаров по названию Z → A")
@allure.description("Проверяет, что товары сортируются корректно от Z к A после выбора соответствующего фильтра.")
@allure.severity(allure.severity_level.NORMAL)
def test_sort_by_name_z_to_a(driver):
    with allure.step("Авторизация"):
        driver.get("https://www.saucedemo.com/v1/")
        username_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")

        password_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("secret_sauce")

        login_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()
        WebDriverWait(driver, 15).until(EC.url_contains("inventory.html"))

    with allure.step("Выбрать сортировку Z → A"):
        sort_dropdown = Select(WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
        ))
        sort_dropdown.select_by_value("za")
        time.sleep(2)

    with allure.step("Собрать список названий товаров"):
        items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        names_list = [item.text for item in items]
        allure.attach(str(names_list), name="Названия товаров", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Проверить, что сортировка выполнена корректно"):
        assert names_list == sorted(names_list, reverse=True), "Ошибка: товары отсортированы неверно"
    print("Сортировка товаров по названию Z → A прошла успешно!")

#  Тест выхода из системы
@allure.title("Выход пользователя из системы")
@allure.description("Проверяет, что пользователь может корректно выйти из системы через боковое меню.")
@allure.severity(allure.severity_level.CRITICAL)
def test_logout(driver):
    driver.get("https://www.saucedemo.com/v1/")

    username_field = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username_field.send_keys("standard_user")

    password_field = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_field.send_keys("secret_sauce")

    login_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()

    WebDriverWait(driver, 15).until(EC.url_contains("inventory.html"))

    # Открываем меню
    burger_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "bm-burger-button"))
    )
    burger_btn.click()
    time.sleep(1)

    logout_link = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "logout_sidebar_link"))
    )
    driver.execute_script("arguments[0].click();", logout_link)

    # Ждём появления кнопки login на странице
    login_button = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )
    assert login_button.is_displayed(), "Кнопка Login не отображается — выход не сработал"
    print("Logout прошёл успешно!")
