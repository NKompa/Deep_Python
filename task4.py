account = 0
operation_count = 0
operation_list = []


def put_money(amount):
    global account, operation_count, operation_list
    if amount % 50 == 0:
        account += amount
        operation_list.append(f"Пополнение: {amount} у.е.")
        operations_count()
    else:
        print("Сумма пополнения должна быть кратной 50 у.е.")


def operations_count():
    global operation_count, account
    operation_count += 1
    if operation_count % 3 == 0:
        account += account * 0.03
        operation_list.append(f"Начисление процентов: {account * 0.03} у.е.")


def take_money(amount):
    global account, operation_count, operation_list
    if amount % 50 == 0:
        if amount <= account:
            fee = amount * 0.015
            if fee < 30:
                fee = 30
            elif fee > 600:
                fee = 600
            account -= amount + fee
            operation_list.append(f"Снятие: {amount} у.е.")
            operation_list.append(f"Комиссия: {fee} у.е.")

            operations_count()

        else:
            print("Недостаточно средств на счете")
    else:
        print("Сумма снятия должна быть кратной 50 у.е.")


def take_tax():
    global account, operation_list
    if account >= 5_000_000:
        tax = account * 0.1
        account -= tax
        operation_list.append(f"Удержание налога: {tax} у.е.")


def print_balance():
    global account
    print(f"Баланс: {account} у.е.\n")


def atm():
    while True:
        print("Выберите действие: \n1. Пополнить счет\n2. Снять со счета\n3. Вывести список операций\n4. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            take_tax()
            amount = int(input("Введите сумму пополнения: "))
            put_money(amount)
            print_balance()

        elif choice == "2":
            take_tax()
            amount = int(input("Введите сумму снятия: "))
            take_money(amount)
            print_balance()

        elif choice == "3":
            print('\n'.join(operation_list))
            print_balance()

        elif choice == "4":
            break

        else:
            print("Неверный выбор, попробуйте снова")


atm()
