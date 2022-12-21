import heapq
from heapq import heappop,heappush,heappushpop
def kthLargestElement(arr,k):
    heap=[]
    for i in range(len(arr)):
        heappush(heap,arr[i])
        if len(heap)>k:
            heappop(heap)
    return heappop(heap)

arr = [6, 5, 3, 2, 8, 10, 9]
k = 3

# print(kthLargestElement(arr,k))


def findClosestElements( arr, k, x) :

    heap = []
    for num in arr:
        heappush(heap,[-abs(x-num),num])
        if len(heap)>k:
            heappop(heap)

    return sorted([ele[1] for ele in heap])
# 3(k) closest number to 12(x)  ,arr=[1,2,13,14,15]
print(findClosestElements([1,2,13,14,15],3,12))



# def maxCost(arr):
#     heap,cost=[],0
#     for ele in arr:
#         heappush(heap,ele)
#     while len(heap)>1:
#         first=heappop(heap)
#         sec=heappop(heap)
#         sum=first+sec
#         cost+=sum
#         heappush(heap,sum)
#     return cost
def maxCost(arr):
    cost=0
    rodWindow=[]
    for i in range(len(arr)):
        heapq.heappush(rodWindow,arr[i])
    while len(rodWindow)>=2:
        first=heapq.heappop(rodWindow)
        sec=heapq.heappop(rodWindow)
        cost+=first+sec
        heapq.heappush(rodWindow,first+sec)
    return cost



print(maxCost([1,2,3,4,5]))