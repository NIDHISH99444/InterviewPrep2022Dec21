

from collections import defaultdict
graph= defaultdict(list)

def addEdge(u ,v):
    graph[u].append(v)
    graph[v].append(u)


def printStru(u):
    for i in range(u):
        print(i ,graph[i])

def checkBipartite(vertex ,visited):
    if visited[vertex]==-1:
        visited[vertex]=1
    for neighbour in graph[vertex]:
        if visited[neighbour] == -1:
            visited[neighbour]=1-visited[vertex]
            if not checkBipartite(neighbour, visited):
                return False
        else:
            if visited[neighbour]==visited[vertex]:
                return False
    return True



addEdge(1, 2)
addEdge(2, 3)
addEdge(3, 4)
addEdge(4, 5)
addEdge(5, 6)
addEdge(5, 7)
addEdge(7, 8)
addEdge(5, 9)
addEdge(9,2)
print(graph)
visited =[-1] *10
# visited[1]=1
print(checkBipartite(1,visited))

print(visited)






