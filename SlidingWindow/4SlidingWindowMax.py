
def slidingWindowMax(arr,k):
    i,j=0,0
    res,fr=[],[]
    while j<len(arr):
        if len(res)!=0 and arr[j]>res[-1]:
            while len(res)!=0 and arr[j]>res[-1]:
                res.pop()
        res.append(arr[j])
        if j-i+1 == k :
            fr.append(res[0])
            if res[0]==arr[i]:
                res.pop(0)
            i+=1
        j+=1

    return fr







nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(slidingWindowMax(nums,k))