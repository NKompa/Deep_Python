data = [1, 2, 1, 4, 7, 9, 23, 13, 5, 4, 23, 9, 9, 1]
duplicates = []
for i in data:
    if data.count(i) > 1:
        if i in duplicates:
            continue
        else:
            duplicates.append(i)
print(duplicates)

duplicates1 = set()
for j in data:
    if data.count(j) > 1:
        duplicates1.add(j)
duplicates1 = list(duplicates1)
print(duplicates1)