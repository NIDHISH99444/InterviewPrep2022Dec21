def uniquePathTD(i,j,dp):
    if i==0 and  j==0:
        return 1
    if i<0 or j<0:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    up=uniquePathTD(i-1,j,dp)
    left=uniquePathTD(i,j-1,dp)
    dp[i][j]=up+left
    return dp[i][j]


m,n=2,2
dp=[[-1 for i in range(n)]for j in range(m)]
#
# print(uniquePathTD(m-1,n-1,dp))

def uniquePathBU(m,n,dp):

    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                dp[i][j]=1
            else:
                if i>0:
                    up=dp[i-1][j]
                else:
                    up=0
                if j>0:
                    left=dp[i][j-1]
                else:
                    left=0
                dp[i][j]=up+left
    return(dp[-1][-1])
m, n = 2, 2
dp = [[-1 for i in range(n)] for j in range(m)]

print(uniquePathBU(m, n, dp))