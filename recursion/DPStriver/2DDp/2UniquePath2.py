

def uniquePathBU(m,n,dp,obs):

    for i in range(m):
        for j in range(n):
            if obs[i][j]==1:
                dp[i][j]=0
            elif i==0 and j==0:
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
    print(dp)
    return(dp[-1][-1])


obs=[[0,0,0],[0,1,0],[0,0,0]]
dp = [[-1 for i in range(len(obs[0]))] for j in range(len(obs))]
m=len(obs)
n=len(obs[0])
print(uniquePathBU(m, n, dp,obs))



