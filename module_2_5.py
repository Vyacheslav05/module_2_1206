n = int(input('Строки (n): ', ))
m = int(input('Столбцы (m): ',  ))
value = int(input('Значение (value): ',  ))
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
matrix = get_matrix(n, m, value)
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

if n <= 0 or m <= 0:
    print('Пустой список')
elif matrix == result1:
    print(matrix)
elif matrix == result2:
    print(matrix)
elif matrix == result3:
    print(matrix)
else:
    print('Введенные значения не сопадают с заданными', matrix)
