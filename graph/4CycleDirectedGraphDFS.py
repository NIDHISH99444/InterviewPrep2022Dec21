

from collections import defaultdict
graph= defaultdict(list)

def addEdge(u ,v):
    graph[u].append(v)


def printStru(u):
    for i in range(u):
        print(i ,graph[i])

def checkCycle(vertex ,visited,dfsvis):

    visited[vertex]=1
    dfsvis[vertex]=1
    for neighbour in graph[vertex]:
        if visited[neighbour] == 1 and dfsvis[neighbour]==1:
            return True
        elif visited[neighbour]!=1:
            if checkCycle(neighbour,visited,dfsvis) :
                return True
    dfsvis[vertex]=0
    return False


def check(vis,dfsvis):
    for i in range(1,10):
        if visited[i]!=1:
            if checkCycle(i,vis,dfsvis):
                return True
    return False

addEdge(1, 2)
addEdge(2, 3)
addEdge(3, 4)
addEdge(4, 5)
addEdge(6, 5)
addEdge(3, 6)
addEdge(7, 2)
addEdge(7, 8)
addEdge(8,9)
addEdge(9,7)
print(graph)
visited =[0] *10
dfsvisited =[0] *10
# visited[1]=1
print(check(visited,dfsvisited))

print(visited)
print(dfsvisited)







