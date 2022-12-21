from heapq import heappop,heappush

nums=[1,1,1,2,2,3]
k = 2


def checkFreq(nums,k):
    freqArr={}
    for ele in nums:
        freqArr[ele]= freqArr.get(ele,0)+1
    heap=[]
    for key,val in freqArr.items():

        heappush(heap,(val,key))
        if k>0:
            k-=1
        else:
            heappop(heap)
    res=[]
    print(heap)
    while heap:
        res.append(heappop(heap)[1])
    return res
print(checkFreq(nums,k))