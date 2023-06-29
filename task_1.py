def to_hex(n):
    hex_digits = '0123456789abcdef'
    hex_string = ''
    hex_prefix = '0x'

    if n == 0:
        return '0'
    while n > 0:
        remainder = n % 16
        hex_digit = hex_digits[remainder]
        hex_string = hex_digit + hex_string
        n = n // 16
    return hex_prefix + hex_string


number = int(input("Введите число: "))

hex_value = to_hex(number)

print("Шестнадцатеричное представление числа:", hex_value)
print("Проверка через функцию hex(): ", hex(number))