names = ["Misha", "Grisha", "Masha"]
rates = [100000, 150000, 130000]
bonus_percent = ["10.25%", "7.5%", "8.75%"]

result = {name: rate * float(bonus[:-1])/100 for name, rate, bonus in zip(names, rates, bonus_percent)}

print(result)