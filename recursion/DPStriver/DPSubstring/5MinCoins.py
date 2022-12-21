

def coinMin(arr,index,target):
    if index<0:
        return float('inf')

    if target==0:
        return 0
    if tap[index][target]!=-1:
        return tap[index][target]
    take=float('inf')
    if target>=arr[index]:
        take=1+coinMin(arr,index,target-arr[index])
    notTake=coinMin(arr,index-1,target)
    tap[index][target]=min(take,notTake)
    return tap[index][target]

coins = [1,2,5]
amount = 11
tap=[[-1 for i in range(amount+1)] for j in range(len(coins)+1)]
res=(coinMin(coins,len(coins)-1,amount))
if res==float('inf'):
    print(-1)
else:
    print(res)