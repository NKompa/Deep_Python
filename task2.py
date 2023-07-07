names = ["Misha", "Grisha", "Masha", "Dasha"]
rates = [100000, 150000, 130000, 160000]
bonus_percent = ["10.25%", "7.5%", "8.75%", "9%"]

result = {name: rate * float(bonus[:-1])/100 for name, rate, bonus in zip(names, rates, bonus_percent)}

print(result)