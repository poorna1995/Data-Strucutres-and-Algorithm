def matrixMultiplication(a,b):
    result = [[0, 0], [0, 0]]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a)):
                result[i][j] += a[i][k] * b[k][j]
    return result


a= [[1,2],[3,4]]
b=[ [5,6], [7,8]]
result = matrixMultiplication(a, b)
print(result)