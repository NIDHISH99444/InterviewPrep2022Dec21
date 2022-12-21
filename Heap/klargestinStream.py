import  heapq

heaplen = 3
heap = [4, 5, 8, 2]
heapq.heapify(heap)
print(heap)
while len(heap)>heaplen:
    heapq.heappop(heap)

def add(ele):
    heapq.heappush(heap,ele)
    if len(heap)>heaplen:
        heapq.heappop(heap)
    return heap[0]




print(add(3))   # return 4
print(add(5))   # return 5
print(add(10))  # return 5
print(add(9))   # return 8
print(add(4))   # return 8