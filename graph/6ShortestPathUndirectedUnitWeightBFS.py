
import sys
from collections import defaultdict
graph= defaultdict(list)

def addEdge(u ,v):
    graph[u].append(v)
    graph[v].append(u)


def printStru(u):
    for i in range(u):
        print(i ,graph[i])

def shortestPath(vertex,distance,queue ):
    distance[vertex]=0
    queue.append(vertex)
    while queue:
        vertex=queue.pop(0)
        for neighbour in graph[vertex]:
            if distance[neighbour]>distance[vertex]+1:
                distance[neighbour]=distance[vertex]+1
                queue.append(neighbour)


addEdge(0, 1)
addEdge(1, 2)
addEdge(2, 6)
addEdge(0, 3)
addEdge(3, 4)
addEdge(4, 5)
addEdge(5, 6)
addEdge(6, 7)
addEdge(6, 8)
addEdge(7, 8)


print(graph)
distance =[100]*9
queue=[]
stack=[]

shortestPath(0,distance,queue)
print("Shortest distance from source to destination from 0 to 6 is ",distance[6])












