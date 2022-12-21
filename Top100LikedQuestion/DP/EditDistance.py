def editDistance(word1,word2,dp):
    for i in range(len(word1)+1):
        dp[i][0]=i
    for j in range(len(word2)+1):
        dp[0][j]=j
    for i in range(1,len(word1)+1):
        for j in range(1,len(word2)+1):
            if word1[i-1]!=word2[j-1]:
                dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
            else:
                dp[i][j]=dp[i-1][j-1]
    print(dp)
    return dp[-1][-1]



word1 = ""
word2 = ""
n=len(word1)
m=len(word2)

dp=[[0 for i in range(m+1)]for j in range(n+1)]
print(editDistance(word1,word2,dp))