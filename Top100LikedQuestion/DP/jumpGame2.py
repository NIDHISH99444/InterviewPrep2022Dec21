def jumpGame(arr,start):
    if start>=len(arr)-1:
        return 0
    if dp[start]!=-1:
        return dp[start]
    minJumps=float("inf")
    for i in range(start+1,start+arr[start]+1):
        minJumps=min(minJumps,1+jumpGame(arr,i))
    dp[start]= minJumps
    return dp[start]





arr=[2,2,0,0,4]
dp=[-1]*len(arr)
print(jumpGame(arr,0))