import heapq
from collections import defaultdict
graph= defaultdict(list)

def addEdge(u ,v,weight):
    graph[u].append([v,weight])
    graph[v].append([u,weight])


def printStru(u):
    for i in range(u):
        print(i ,graph[i])

def dijkistras(vertex,distance):
    distance[vertex] = 0
    heap=[]
    heapq.heappush(heap,(0,vertex))
    while heap:
        dis,node=heapq.heappop(heap)
        for neighbour in graph[node]:
            if distance[neighbour[0]]>dis+neighbour[1]:
                distance[neighbour[0]] = dis + neighbour[1]
                heapq.heappush(heap,(distance[neighbour[0]] ,neighbour[0]))

addEdge(1, 2 ,2)
addEdge(2, 5 ,5)
addEdge(1, 4 ,1)
addEdge(4, 3 ,3)
addEdge(3, 2 ,4)
addEdge(3, 5 ,1)

print(graph)
visited =[0] *10
print(visited)
distance =[100] *6
dijkistras(1,distance)
print("distance of individual node from root is ",distance[1:])









