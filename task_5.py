from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
NUM_ATTEMPTS = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Угадайте число от %d до %d. У вас есть %d попыток." % (LOWER_LIMIT, UPPER_LIMIT, NUM_ATTEMPTS))

for attempt in range(1, NUM_ATTEMPTS + 1):
    guess = int(input("Попытка %d: " % attempt))

    if guess < num:
        print("Загаданное число больше")
    elif guess > num:
        print("Загаданное число меньше")
    else:
        print("Поздравляем! Вы угадали число за %d попыток." % attempt)
        break

if guess != num:
    print("К сожалению, вы исчерпали все попытки. Загаданное число было %d." % num)