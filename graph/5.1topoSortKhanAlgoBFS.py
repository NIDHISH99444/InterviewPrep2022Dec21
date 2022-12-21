# first we will calculate the indegree of all the node
# then we will put the node with  0 indegree in queue
#iterate through queue ,pop ele from q , check for its neighbours , reduce there indegree by one , once the indegree is 0 ,add then in the queue

from collections import defaultdict

def addEdge(u,v):
    graph[u].append(v)


def topologicalSortKhansAlgoBFS():
    for val in graph.values():
        for ele in val:
            indegree[ele]+=1
    print(indegree)
    q=[]
    for index,val in enumerate(indegree):
        if val==0:
            q.append(index)
    res=[]
    while q :
        nextEle=q.pop(0)
        res.append(nextEle)
        for neighbour in graph[nextEle]:
            indegree[neighbour]-=1
            if indegree[neighbour]==0:
                q.append(neighbour)
    return (res)








graph=defaultdict(list)

addEdge(5, 0)
addEdge(5, 2)
addEdge(4, 0)
addEdge(4, 1)
addEdge(2, 3)
addEdge(3, 1)


print(graph)
indegree=[0]*(len(graph)+2)
print(topologicalSortKhansAlgoBFS())


