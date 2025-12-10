price = float(input("Введите цену товара:"))
promo = input("Естли ли промокод(да/нет)")

discount = 0 

# Скидка за цену 
if price > 1000:
    discount += 10

# Скидка за промокод
if promo == "да":
    discount += 5

final_price = price - (price * discount / 100)
print(f"Скидка: {discount}%")
print(f"Итоговая цена {final_price}")