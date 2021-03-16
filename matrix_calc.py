# matrix transpose, sum, scale

a = [[1, 2, 3], [-2, 0, -1]]
b = [[10, 20, 30],[100, 200, 300]]


def show(matrix):
    string_matrix = ''
    for i in matrix:
        for j in i:
            string_matrix += str(j) + '\t'
        string_matrix += '\n'
    return string_matrix


def transpose(matrix):
    transposed_matrix = []
    for j in range(len(matrix[0])):
        row = []
        for i in matrix:
            row.append(i[j])
        transposed_matrix.append(row)
    return transposed_matrix


def matrix_sum(matrix1, matrix2):
    res_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        res_matrix.append(row)
    return res_matrix

def matrix_scale(matrix, sc):
    res_matrix = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j * sc)
        res_matrix.append(row)
    return res_matrix

print(show(a))
print(show(transpose(a)))
print(show(matrix_sum(a,b)))
print(show(matrix_scale(a, 2)))