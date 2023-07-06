def transpose_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


matrix1 = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]]
for row in transpose_matrix(matrix1):
    print(row)