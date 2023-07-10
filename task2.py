"""Function checks the position of 8 queens on the chess board:

 if any queen can beat another one - False, if no queen can beat another - True"""


def check_queens(tuple_list):
    for i in range(len(tuple_list)):
        for j in range(i + 1, len(tuple_list)):
            x_diff = abs(tuple_list[i][0] - tuple_list[j][0])
            y_diff = abs(tuple_list[i][1] - tuple_list[j][1])
            if tuple_list[i][0] == tuple_list[j][0] or tuple_list[i][1] == tuple_list[j][1] or x_diff == y_diff:
                return False
    return True


if __name__ == "__main__":
    queens1 = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 3), (6, 1), (7, 7), (8, 5)]
    queens2 = [(1, 1), (2, 4), (3, 6), (4, 8), (5, 3), (6, 1), (7, 7), (8, 5)]
    result1 = check_queens(queens1)
    result2 = check_queens(queens2)
    print(result1)
    print(result2)