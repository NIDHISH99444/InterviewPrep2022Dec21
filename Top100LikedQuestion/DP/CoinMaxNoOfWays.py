def maxCoin(coins,sum):
    n=len(coins)
    dp=[[0 for i in range(sum+1)]for j in range(n+1)]
    for i in range(len(dp)):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if coins[i-1]<=j:
                dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    print(dp)

    return dp[-1][-1]


sum = 4
N = 3
coins = [1,2,3]
print(maxCoin(coins,sum))