

#memoization solution (top down)
def fibo(n):
    if n<=1:
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n]=fibo(n-1)+fibo(n-2)
    return dp[n]


n=5
dp=[-1]*(n+1)
print(fibo(n))
#tabulation solution (bottom up)

def fibb(n):
    dp=[-1]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[-1]

n=5
print(fibb(5))


