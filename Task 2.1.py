money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
summa = money_capital+salary
month = 0
summa = summa-spend
while summa >= 0:
    summa = summa - spend * (1 + increase)
    summa = summa + salary
    month = month+1
    spend = spend*(1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", month)
