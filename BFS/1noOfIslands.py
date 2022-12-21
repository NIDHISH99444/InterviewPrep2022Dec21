
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    cnt = 0
    print(grid)
    n = len(grid)
    m = len(grid[0])
    queue=[]
    visited=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] =="1" and visited[i][j]==0:
                cnt+=1
                queue.append((i, j))
                move(grid,visited,i,j,queue)

    return  cnt

def move(grid,visited,i,j,queue):
    visited[i][j]=1
    row=[-1,0,1,0]
    col=[0,1,0,-1]
    while queue:
        i,j=queue.pop(0)
        for index in range(len(row)):
            newr=row[index]+i
            newc=col[index]+j
            if newr>=0 and newr<len(grid) and newc>=0 and newc<len(grid[0]) and  visited[newr][newc]==0 and grid[newr][newc]=="1" :
                print(newr,newc,i,j)
                visited[newr][newc]=1
                queue.append((newr,newc))



grid  = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","1","0","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))
