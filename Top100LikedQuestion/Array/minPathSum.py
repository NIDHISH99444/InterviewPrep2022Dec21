


def minPath(grid):
    newmat=[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    newmat[0][0]=grid[0][0]
    print(newmat)
    for i in range(1,len(grid)):
        newmat[i][0]=newmat[i-1][0]+grid[i][0]
    for i in range(1, len(grid[0])):
        newmat[0][i]=newmat[0][i-1]+grid[0][i]
    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
            newmat[i][j]=min(newmat[i-1][j],newmat[i][j-1])+grid[i][j]

    return newmat[len(grid)-1][len(grid[0])-1]


grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPath(grid))