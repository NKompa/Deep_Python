num = int(input("Введите число для проверки: "))

if num < 1:
    print("Число должно быть больше или равно 1")
elif num > 100000:
    print("Число должно быть меньше или равно 100000")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Число является простым")
    else:
        print("Число является составным")