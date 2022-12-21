def minPathSum(grid,dp,i,j):
    if i==0 and j==0:
        return grid[0][0]
    if i<0 or j<0:
        return float('inf')
    if dp[i][j]!=-1:
        return dp[i][j]
    up=minPathSum(grid,dp,i-1,j)
    left=minPathSum(grid,dp,i,j-1)
    dp[i][j]=min(up,left)+grid[i][j]
    return dp[i][j]





grid = [[1,2,3],[4,5,6]]
dp = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
m=len(grid)-1
n=len(grid[0])-1

print(minPathSum(grid,dp,m,n))
print(dp)