

def subsetSum(a, index, target):
    if target==0:
        return True
    if index<0:
        return False
    # if index==0:
    #     if a[index]==target:
    #         return True
    if tab[index][target]!=-1:
        return tab[index][target]
    nottake=subsetSum(a,index-1,target)
    take = False
    if a[index] <=target:
        take = subsetSum(a, index - 1, target - a[index])

    tab[index][target]=take or nottake
    return tab[index][target]



a = [1,2,4]
n=len(a)-1
sum = 3


tab = [[-1 for i in range(len(a)+1)] for j in range(sum+1)]

print(subsetSum(a, n, sum))




