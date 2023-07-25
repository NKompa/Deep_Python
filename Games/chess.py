import random


def check_queens(tuple_list):
    for i in range(len(tuple_list)):
        for j in range(i + 1, len(tuple_list)):
            x_diff = abs(tuple_list[i][0] - tuple_list[j][0])
            y_diff = abs(tuple_list[i][1] - tuple_list[j][1])
            if tuple_list[i][0] == tuple_list[j][0] or tuple_list[i][1] == tuple_list[j][1] or x_diff == y_diff:
                return False
    return True


def generate_position():
    max_position = 8
    position = []
    for i in range(1, max_position + 1):
        position.append((i, random.randint(1, max_position)))
    return position


def find_good_position():
    count = 0
    while count < 4:
        new_position = generate_position()
        if check_queens(new_position):
            print(new_position)
            count += 1


if __name__ == "__main__":
    find_good_position()
