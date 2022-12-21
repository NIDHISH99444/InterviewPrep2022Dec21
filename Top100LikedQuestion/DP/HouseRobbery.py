


def houseRobbery(arr,index,dp):
    if index==0:
        return arr[index]
    if index==-1:
        return 0
    if dp[index]!=-1:
        return  dp[index]
    pick = arr[index]+houseRobbery(arr,index-2,dp)
    notpick = houseRobbery(arr,index-1,dp)
    dp[index]=max(pick,notpick)
    return dp[index]

arr = [1,2,3,1]
n=len(arr)-1
dp=[-1]*(len(arr))
print(houseRobbery(arr,n,dp))

def houseRobbery1(arr):
    if len(arr) == 1:
        return arr[0]
    dp=[0]*len(arr)
    dp[0]=arr[0]
    for i in range(1,len(arr)):
        if i-2<0:
            pick=0
        else:
            pick=dp[i-2]
        dp[i]=max(arr[i]+pick,dp[i-1])
    return dp[-1]


def houseRobbery2(arr):
    arr1=arr[:]
    arr2=arr[:]
    return max(houseRobbery1(arr1[1:]),houseRobbery1(arr2[:-1]))

arr = [1,2,3,1]
print(houseRobbery2(arr))