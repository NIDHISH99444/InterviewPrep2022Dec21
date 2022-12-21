

from collections import defaultdict
graph= defaultdict(list)

def addEdge(u ,v,weight):
    graph[u].append([v,weight])


def printStru(u):
    for i in range(u):
        print(i ,graph[i])

def topologicalDFS(vertex ,stack):
    visited[vertex]=1
    for neighbour in graph[vertex]:
        if visited[neighbour[0]]!=1:
                topologicalDFS(neighbour[0],stack)
    stack.append(vertex)


def getTopologicalOrder(vis,stack):
    for i in range(0,6):
        if vis[i]!=1:
            topologicalDFS(i,stack)
    print("Topological Ordering is : ")
    return  stack

def findingShortestPath(stack,distance):
    element = stack.pop()
    distance[element] = 0
    while(stack):
        for neighbour in graph[element]:
            if distance[neighbour[0]]>distance[element]+neighbour[1]:
                distance[neighbour[0]] = distance[element] + neighbour[1]
        element = stack.pop()

addEdge(0, 1 ,2)
addEdge(1, 2 ,3)
addEdge(2, 3 ,6)
addEdge(0, 4 ,1)
addEdge(4, 2 ,2)
addEdge(4, 5 ,4)
addEdge(5, 3, 1)


print(graph)
visited =[0] *10
print(visited)
stack=[]
stack =getTopologicalOrder(visited,stack)
print(stack[::-1])
distance =[100] *6
findingShortestPath(stack,distance)
print("distance of individual node from root is ",distance)









