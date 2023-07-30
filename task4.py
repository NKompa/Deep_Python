class Matrix:
    """Class Matrix performs different operations with matrices of the same size"""
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "Матрица:\n" + '\n'.join([str(row) for row in self.matrix])

    def __repr__(self):
        return f"Matrix({self.matrix})"

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матрицы должны быть одинакового размера.")

        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)

        return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матрицы должны быть одинакового размера.")

        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                element = sum([self.matrix[i][k] * other.matrix[k][j] for k in range(len(other.matrix))])
                row.append(element)
            result.append(row)

        return Matrix(result)


if __name__ == "__main__":
    matrix1 = Matrix([[1, 2, 3], [10, 10, 10]])
    matrix2 = Matrix([[7, 8, 9], [20, 20, 20]])
    print(matrix1)
    print(matrix2)
    print(matrix1 == matrix2)
    print(matrix1 + matrix2)
    print(matrix1 * matrix2)