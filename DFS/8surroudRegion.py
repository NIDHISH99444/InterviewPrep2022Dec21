


def surround(board):
    n=len(board)
    m=len(board[0])
    visited=[[0 for i in range(m)]for j in range(n)]
    arr0=[0,m-1]
    arr1=[0,n-1]
    for ele in arr0:
        for k in range(n):
            # print("here",k,ele)
            if board[k][ele]=="O":
                # print("inside arr0 ", k, ele)
                dfs(board,k,ele,visited)
    for ele in arr1:
        for k in range(m):
            # print("there",ele,k)
            if board[ele][k]=="O":
                # print("inside arr1 ",ele,k)
                dfs(board,ele,k,visited)
    print(visited)
    for i in range(n):
        for j in range(m):
            if visited[i][j]==1:
                board[i][j]='O'
            else:
                board[i][j]='X'
    return (board)

def dfs(board,i,j,visited):
    visited[i][j]=1
    row=[-1,0,1,0]
    col=[0,1,0,-1]
    for index in range(len(row)):
        down=i+row[index]
        right=j+col[index]
        print("index",down,right)
        if down>=0 and down<len(board) and right>=0 and right<len(board[0]) and  visited[i+row[index]][j+col[index]]!=1 and board[i+row[index]][j+col[index]]=='O':
            print("changed",i+row[index],j+col[index])
            visited[i+row[index]][j+col[index]]=1
            dfs(board,i+row[index],j+col[index],visited)



board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
print(surround(board))