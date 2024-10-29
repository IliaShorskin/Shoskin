salary = 5000 
spend = 6000  
months = 10  
increase = 0.03  
money_capital = spend - salary
for i in range(months - 1):
    money_capital = money_capital + (spend * (1 + increase) - salary)
    spend = spend * (1 + increase)
money_capital = int(round(money_capital))
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)