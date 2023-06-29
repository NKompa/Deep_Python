import fractions


def split_fraction(fraction):
    nums = fraction.split('/')
    numerator = int(nums[0])
    denominator = int(nums[1])
    return numerator, denominator


def find_max_divider(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def sum_fractions(fraction1, fraction2):
    num1, den1 = split_fraction(fraction1)
    num2, den2 = split_fraction(fraction2)

    sum_num = (num1 * den2 + num2 * den1)
    sum_den = den1 * den2

    gcd_num = find_max_divider(sum_num, sum_den)
    result_num = sum_num // gcd_num
    result_den = sum_den // gcd_num

    return f"{result_num}/{result_den}"


def mult_fractions(fraction1, fraction2):
    num1, den1 = split_fraction(fraction1)
    num2, den2 = split_fraction(fraction2)

    mult_num = num1 * num2
    mult_den = den1 * den2

    gcd_num = find_max_divider(mult_num, mult_den)
    result_num = mult_num // gcd_num
    result_den = mult_den // gcd_num
    return f"{result_num}/{result_den}"


f1 = input("Введите первую дробь вида а/b: ")
f2 = input("Введите вторую дробь вида а/b: ")

print("Сумма дробей = " + sum_fractions(f1, f2))
print("Произведение дробей = " + mult_fractions(f1, f2))

frac1 = fractions.Fraction(*split_fraction(f1))
frac2 = fractions.Fraction(*split_fraction(f2))
print(f"Проверка суммы функцией fraction(): {frac1 + frac2}")
print(f"Проверка произведения функцией fraction(): {frac1 * frac2}")