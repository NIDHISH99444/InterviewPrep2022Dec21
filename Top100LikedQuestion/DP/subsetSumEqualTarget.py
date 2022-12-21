

def subsetSumEqualTarget(arr,sum) :
    n=len(arr)+1
    t=[[0 for i in range(sum+1)]for j in range(n)]
    print(t)

    for i in range(n):
        t[i][0]=1
    for i in range(1,n):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]
            else:
                t[i][j] = t[i - 1][j]
    return t[-1][-1]

def checksum(arr):
    if sum(arr)%2!=0:
        return False
    else:
        computedSum=sum(arr)// 2
        index = 0
        if subsetSumEqualTarget(arr, computedSum):
            return True
        else:
            return False
arr=[1,5,11,5]
print(checksum(arr))

