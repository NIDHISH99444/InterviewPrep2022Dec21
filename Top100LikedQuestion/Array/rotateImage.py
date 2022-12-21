



def rotate(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(n):
            if i<j :
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    print(matrix)

    for i in range(n):
        for j in range(n//2):
            matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]
    print(matrix)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)