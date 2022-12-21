


def uniquePath(m,n):
    matrix=[[0 for i in range(n)] for j in range(m)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i==0 or j==0:
                matrix[i][j]=1
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]

    return matrix[len(matrix)-1][len(matrix[0])-1]
m = 3
n = 7
print(uniquePath(m,n))