def fibonacci_generator(num):
    a, b = 0, 1
    count = 0
    while count < num:
        yield a
        a, b = b, a + b
        count += 1


for i in fibonacci_generator(15):
    print(i, end=" ")