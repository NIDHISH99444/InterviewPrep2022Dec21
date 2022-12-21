

def subsetSum(a, index, target):
    if target==0:
        return 1
    if index<0:
        return 0
    # if index==0:
    #     if a[index]==target:
    #         return True
    if tab[index][target]!=-1:
        return tab[index][target]
    nottake=subsetSum(a,index-1,target)
    take = 0
    if a[index] <=target:
        take = subsetSum(a, index - 1, target - a[index])

    tab[index][target]=take + nottake
    return tab[index][target]


arr = [1, 2, 3]
X = 3
tab=[[-1 for i in range(X+1)]for j in range(len(arr)+1)]
print(subsetSum(arr,len(arr)-1,X))

