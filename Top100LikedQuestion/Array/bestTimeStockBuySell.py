


def bestTime(arr):
    minv,res=arr[0],0
    for i in range(1,len(arr)):
        minv=min(minv,arr[i])
        res=max(res,arr[i]-minv)
    return  res


prices = [7,6,4,3,1]
print(bestTime(prices))