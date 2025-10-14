# Список товаров (имитация ответа с сервера)
products = [
    {"name": "Рюкзак", "price": 29.99},
    {"name": "Фонарик", "price": 9.99},
    {"name": "Футболка", "price": 15.99},
]

# Сортировка по цене (от низкой к высокой)
products_sorted = sorted(products, key=lambda x: x["price"])

# Вывод результата
print("Товары по цене (от низкой к высокой):")
for p in products_sorted:
    print(f"{p['name']} — ${p['price']}")
