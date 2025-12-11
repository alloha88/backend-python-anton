# Список трат за день 
expenses = [300, 900, 1200, 500, 4500]

# Сумма трат 1 
total = 0 
for x in expenses:
    total += x

#Средняя трата 
average = total/len(expenses)

# Максимальные траты
maximum = expenses[0]
for x in expenses:
    if x > maximum:
        maximum = x

# Считаем траты > 1000
big_count = 0
for x in expenses:
    if x > 1000:
        big_count += 1
print(f"Траты:{expenses}")
print(f"Общая сумма:{total}")
print(f"Средняя трата:{average}")
print(f"Максимальная трата:{maximum}")
print(f"Трат больше 1000:{big_count}")