
#top down /memoization
def frogJump(arr,index):
    if index==0:
        return 0
    if dp[index]!=-1:
        return dp[index]
    left=frogJump(arr,index-1)+abs(arr[index]-arr[index-1])
    right=float('inf')
    if index>1:
        right=min(frogJump(arr,index-2),right)+abs(arr[index]-arr[index-2])
    dp[index]=min(left,right)
    return dp[index]



arr=[30,10,60,10,60,50]
dp=[-1]*(len(arr))
print(frogJump(arr,5))
print(dp)

# bottom up (tabulisation)

def frogJumpBU(arr,index):
    dp=[0]*len(arr)
    if index==0:
        dp[0]=0
    for i in range(1,len(arr)):
        left=dp[index-1]+abs(arr[index]-arr[index-1])
        right=float('inf')
        if index>1:
            right=dp[index-2]+abs(arr[index]-arr[index-2])
    dp[index]=min(left,right)
    return dp[index]


arr=[30,10,60,10,60,50]

# print(frogJumpBU(arr,5))
# print(dp)


# def frogJumpK(arr,index,k):
#     if index==0:
#         return 0
#     # if dp[index]!=-1:
#     #     return dp[index]
#     for i in range(1,k):
#         if index-k>=0:
#             val=frogJumpK(arr,index-i,k)+abs(arr[index]-arr[index-i])
#             print(val)
#             res=min(res,val)
#     return res
#
#
# arr=[30,10,60,10,60,50]
#
# print(frogJumpK(arr,5,2))
# print(dp)
#
