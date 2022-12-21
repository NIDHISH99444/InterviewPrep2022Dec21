
def coinMaxWays(arr,index,target):
    if index<0:
        return 0
    if target==0:
        return 1
    if tap[index][target]!=-1:
        return tap[index][target]
    take=0
    if target>=arr[index]:
        take=coinMaxWays(arr,index,target-arr[index])
    notTake=coinMaxWays(arr,index-1,target)
    tap[index][target]=(take+notTake)
    return tap[index][target]

coins = [1,2,5]
amount = 5
tap=[[-1 for i in range(amount+1)] for j in range(len(coins)+1)]
res=(coinMaxWays(coins,len(coins)-1,amount))
print(res)
