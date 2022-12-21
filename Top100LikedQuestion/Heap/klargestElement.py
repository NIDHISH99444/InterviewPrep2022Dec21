

from heapq import heappop,heappush

def kthLargest(nums,k):
    heap=[]
    for i in range(len(nums)):
        heappush(heap,nums[i])
        if len(heap)>k:
            heappop(heap)
    return heappop(heap)


nums = [3,2,1,5,6,4]
k = 2

print(kthLargest(nums,k))
