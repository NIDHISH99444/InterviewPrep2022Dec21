
def issafe(visited,row,col):
    dupr=row
    dupc=col
    while row>=0 and col>=0:
        if visited[row][col]=='Q':
            return False
        else:
            row-=1
            col-=1
    row=dupr
    col=dupc
    while col>=0:
        if visited[row][col]=='Q':
            return False
        else:
            col-=1
    row = dupr
    col = dupc
    while row<len(visited) and col>=0:
        if visited[row][col]=='Q':
            return False
        else:
            row+=1
            col-=1
    return  True


matrix=[]
def nqueen(visited,col):

    for i in range(len(visited)):
        if col==len(visited[0]):
            res=[]
            for ele in visited:
                res.append("".join(ele))

            matrix.append(res)
            return
        if issafe(visited,i,col):
            visited[i][col]='Q'
            nqueen(visited,col+1)
            visited[i][col] = '.'


n=4
visited=[['.' for i in range(n)]for j in range(n)]

nqueen(visited,0)
print(matrix)