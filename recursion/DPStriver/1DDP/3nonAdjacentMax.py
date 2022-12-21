

def findNonAdjacentMax(arr,index):
    if index<0:
        return 0
    if dp[index]!=-1:
        return dp[index]
    take=arr[index]+findNonAdjacentMax(arr,index-2)
    notTake=findNonAdjacentMax(arr,index-1)
    dp[index]=max(take,notTake)
    return dp[index]


arr= [5, 7, 10, 100, 10, 5]
dp=[-1]*(len(arr))
print(findNonAdjacentMax(arr,5))


