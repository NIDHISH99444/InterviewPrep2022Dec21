from heapq import  heappop,heappush

points = [[3,3],[5,-1],[-2,4]]
k = 2
def closest(points,k):
    heap=[]
    for ele in points:
        res=ele[0]**2+ele[1]**2
        heappush(heap,[-res,[ele[0],ele[1]]])
        if len(heap)>k:
            heappop(heap)
    res=[]
    while heap:
        res.append(heappop(heap)[1])

    print(res)


closest(points,k)