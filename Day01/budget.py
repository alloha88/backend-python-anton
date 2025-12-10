budget = float(input("Сколько денег у тебя на сегодня? "))
food = float(input("Сколько денег потратил на еду?"))
transport = float(input("Сколько потратил на транспорт?"))
other = float(input("Сколько потратил на покупки?"))

total_spent = food + transport + other
remaining = budget - total_spent

print(f"Всего потрачено:,  {total_spent}")
print(f"Осталось денег:,  {remaining}")