import sqlite3
from collections import defaultdict
graph= defaultdict(list)

def printStru(u):
    for i in range(u):
        print(i ,graph[i])


def check(vis):
    inorder,queue=[0]*numCourses,[]
    res=[]
    if prerequisites == [] or prerequisites[0] == []:
        return [i for i in range(numCourses - 1, -1, -1)]
    for vertex in range(numCourses):
        for neighbour in graph[vertex]:
            inorder[neighbour]+=1
    print("inorder",inorder)
    for index,ele in enumerate(inorder):
        if ele==0:
            queue.append(index)

    cnt=1
    print("que",queue)
    while queue:
        vertex=queue.pop(0)

        res.append(vertex)
        print("res",res)
        for neighbour in graph[vertex]:
            inorder[neighbour] -= 1
            if inorder[neighbour]==0:
                queue.append(neighbour)
                cnt+=1
    print("inorder",inorder)
    if len(inorder):
        return res
    else:
        return  []



    for i in range(0,numCourses):
        if vis[i]!=1:
            topologicalDFS(i,stack)
    topolist=[]
    while stack:
        topolist.append(stack.pop())
    return  topolist

numCourses =  3
prerequisites = [[1,0]]
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]

for ele in prerequisites:
    graph[ele[1]].append(ele[0])
print(graph)
visited =[0] * numCourses


print(check(visited))











