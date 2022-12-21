def minnoOfCoins(coins,amount):
    dp=[[0 for i in range(amount+1)]for j in range(len(coins)+1)]
    print(dp)
    for i in range(1,amount+1):
        dp[0][i]=amount+1

    for i in range(1,len(coins)+1):
        for j in range(1,amount+1):
            if coins[i-1]<=j:
                dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i-1]])
            else:
                dp[i][j]=dp[i-1][j]
    print(dp)
    if dp[-1][-1] == amount+1:
        return -1
    return  dp[-1][-1]

coins = [1,2,5]
amount = 11
print(minnoOfCoins(coins,amount))