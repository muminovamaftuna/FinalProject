import requests

BASE_URL = "https://www.saucedemo.com/v1"

def test_login_valid_user():
    response = requests.get(f"{BASE_URL}/index.html")  # просто проверяем доступность
    assert response.status_code == 200, "Ошибка: сайт недоступен"
    print("Сайт доступен, логин-страница открывается")
