



def climbStair(n,dp):
    if n==1 or n==0:
        return 1
    if dp[n]!=-1:
        return dp[n]
    dp[n]=climbStair(n-1,dp)+climbStair(n-2,dp)
    return  dp[n]





n=4
dp=[-1]*(n+1)
print(climbStair(n,dp))