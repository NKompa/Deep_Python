n = int(input("Введите количество рядов в ёлке: "))

max_width = n * 2 - 1

for i in range(n):
    star_count = i * 2 + 1
    space_count = max_width - star_count

    for j in range(space_count // 2):
        print(" ", end="")

    for j in range(star_count):
        print("*", end="")

    print()