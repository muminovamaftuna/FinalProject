import time
import requests
import statistics

BASE_URL = "https://www.saucedemo.com/v1/"

def test_inventory_page_performance_soft():

    response_times = []  # список для хранения времени каждого запроса

    print("\nЗапуск мягкого теста производительности (10 последовательных запросов)...\n")

    for i in range(10):  # выполняем 10 запросов подряд
        start_time = time.time()
        try:
            response = requests.get(BASE_URL)
            elapsed = time.time() - start_time
            response_times.append(elapsed)

            # Проверка, что сервер отвечает успешно
            if response.status_code != 200:
                print(f"Ошибка: сайт не ответил (код {response.status_code})")
            else:
                print(f"Запрос {i + 1}: {elapsed:.3f} сек")
        except requests.RequestException as e:
            print(f"Запрос {i + 1} завершился ошибкой: {e}")

    if not response_times:
        print("Не удалось выполнить ни одного запроса. Тест завершён.")
        return

    # Расчёт статистики
    avg_time = statistics.mean(response_times)
    max_time = max(response_times)
    min_time = min(response_times)

    print("\nРезультаты теста:")
    print(f"Минимальное время отклика: {min_time:.3f} сек")
    print(f"Среднее время отклика:     {avg_time:.3f} сек")
    print(f"Максимальное время отклика: {max_time:.3f} сек")

    # Критерии оценки (мягкий режим)
    if avg_time > 5.0:
        print(f"Критическая задержка! Среднее время отклика: {avg_time:.3f} сек")
    elif avg_time > 1.0:
        print(f"Медленно, но в пределах допустимого ({avg_time:.3f} сек)")
    else:
        print("Отличная производительность (<1 сек)")

    print("\nМягкий тест завершён")
