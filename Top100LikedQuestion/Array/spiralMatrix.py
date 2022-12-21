


def spiral(matrix):
    k,s=0,0
    res=[]
    m,l=len(matrix)-1,len(matrix[0])-1
    while k< m and s < l :
        for i in range(s,l+1):
            res.append(matrix[k][i])
        k+=1
        for i in range(k,m+1):
            res.append(matrix[i][l])
        l-=1
        for i in range(l,s-1,-1):
            res.append(matrix[m][i])
        m-=1
        for i in range(m,k-1,-1):
            res.append(matrix[i][s])
        s+=1

    if k==m :
        for i in range(s,l+1):
            res.append(matrix[k][i])
    if s==l and k!=m:
        for i in range(k,m+1):
            res.append(matrix[i][s])

    return  res

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiral(matrix))