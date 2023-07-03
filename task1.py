data = input("Введите текст: ").lower()
ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
new_dic = {}
for i in data:
    if i in ru_alphabet:
        new_dic[i] = data.count(i)
print(new_dic)

for j in data:
    count_j = 0
    if j in ru_alphabet:
        count_j += 1
        continue
        new_dic[j] = count_j
print(new_dic)