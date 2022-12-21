

def maze(board,visited,i,j,finalString):
    if i==len(board)-1 and j==len(board[0])-1:
        print(finalString)
        return
    visited[i][j]=1
    rows=[1,0,0,-1]
    cols=[0,-1,1,0]
    string=['D','L','R','U']
    for index in range(len(rows)):
        nextrow=i+rows[index]
        nextcol=j+cols[index]
        if nextrow>=0 and nextrow<len(board) and nextcol>=0 and nextcol<len(board[0]) and visited[nextrow][nextcol]==0 and board[nextrow][nextcol]==1:
            visited[nextrow][nextcol]=1
            maze(board,visited,nextrow,nextcol,finalString + string[index])
            visited[nextrow][nextcol]=0





board=[[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
n=len(board)
m=len(board[0])
i,j=0,0
visited=[[0 for i in range(m)] for j in range(n)]
maze(board,visited,i,j,'')
