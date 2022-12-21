


def rodCuttingMax(cost,length,index,target):
    if index<0:
        return float('-inf')
    if target==0:
        return 0
    if tap[index][target]!=-1:
        return tap[index][target]
    take=float('-inf')
    if length[index]<=target:
        take=cost[index]+rodCuttingMax(cost,length,index,target-length[index])
    notTake=rodCuttingMax(cost,length,index-1,target)
    tap[index][target]=max(take,notTake)
    return tap[index][target]

n=7
length=[]
for i in range(n):
    length.append(i+1)

cost=[1,3,3,3,4,4,6]


target=n
tap=[[-1 for i in range(n+1)]for j in range(n+1)]
print(rodCuttingMax(cost,length,n-1,target))


