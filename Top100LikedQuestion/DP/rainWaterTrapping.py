def rainwater(arr):
    maxl,maxr=[0]*len(arr),[0]*len(arr)
    maxl[0],maxr[len(arr)-1]=arr[0],arr[len(arr)-1]
    for i in range(1,len(arr)):
        maxl[i]=max(arr[i],maxl[i-1])
    for j in range(len(arr)-2,-1,-1):
        maxr[j] = max(arr[j], maxr[j+1])
    totsum=0
    for i in range(len(arr)):
        totsum+=min(maxr[i],maxl[i])-arr[i]
    return totsum








height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(rainwater(height))