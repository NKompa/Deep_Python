for i in range(2, 10, 4):
    for j in range(2, 11):
        for k in range(i, i+4):
            if k <= 9:
                print(f"{k} x {j} = {k*j}\t", end="")
        print()
    print()