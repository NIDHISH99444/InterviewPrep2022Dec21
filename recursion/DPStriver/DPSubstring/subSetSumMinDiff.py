

def subsetSum(a, index, target,dp):
    for i in range(len(dp)):
        dp[i][0]=True
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if a[i-1]<=j:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-a[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    return (dp[-1])




a = [1,2,4]
n=len(a)
sumtotal = 3


dp = [[False for i in range(n+1)] for j in range(sumtotal+1)]

res=subsetSum(a, n, sum,dp)
resList = []
for index, value in enumerate(dp[-1]):
    if value:
        resList.append(index)
sumVal = sum(a)
minDiff = float('inf')
for ele in resList:
    s1=ele
    s2=sumVal-ele
    minDiff = min(minDiff, abs(s1 - s2))

print(minDiff)

