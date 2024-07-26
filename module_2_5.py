#module_2_5

def get_matrix(n, m, value):
    matrix = []
    for i in range(0, n):
        matrix.append([])
        for j in range(0, m):
            matrix[i].append([])
            matrix[i][j] = value
    return matrix



n = int(input("Введите кол-во строк: "))
m = int(input("Введите кол-во столбцов: "))
value = float(input("Введите значение: "))
matrix = get_matrix(n, m, value)
print(matrix)


