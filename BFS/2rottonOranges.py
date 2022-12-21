
def rottonOranges(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    cntFresh = 0
    n = len(grid)
    m = len(grid[0])
    queue,maxtime=[],0
    visited=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] ==1 :
                cntFresh+=1
            elif grid[i][j]==2:
                visited[i][j]=2
                queue.append((i,j,0))
    cnt=0
    while queue:
        i,j,time=queue.pop(0)
        row=[-1,0,1,0]
        col=[0,1,0,-1]
        maxtime=max(maxtime,time)
        for index in range(len(row)):
            newr=row[index]+i
            newc=col[index]+j
            if newr>=0 and newr<len(grid) and newc>=0 and newc<len(grid[0]) and visited[newr][newc]!=2 and grid[newr][newc]==1 :
                cnt+=1
                visited[newr][newc]=2
                queue.append((newr,newc,time+1))
    if cnt!=cntFresh:
        return -1
    else:
        return  maxtime

grid  =[[0,2]]
print(rottonOranges(grid))
