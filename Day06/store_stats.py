prices = {
    "Хлеб": 50,
    "Молоко": 120,
    "Яйца": 180,
    "Свинина": 550,
    "Вода": 40,
    "Курица": 390,
    "Яблоки": 100
}

#1. Общая сумма
total = 0 
for price in prices.values():
    total += price
#2. Самый дорогой товар 
max_price = 0 
max_product = ""

for name, price in prices.items():
    if price > max_price:
        max_price = price
        max_product = name
#3. Товары дороже 100 
print("Товары дороже 100:")
for name, price in prices.items():
    if price > max_price:
        print(name, price)

print("------Прайс-------")
print("Общая сумма:", total)
print("Самый дорогой товар:", max_product, max_price)