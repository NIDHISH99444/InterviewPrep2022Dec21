
def checkExists(matrix,i,j,word,count):
    if len(word)==count:
        return True
    if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]!=word[count]:
        return False
    temp=matrix[i][j]
    matrix[i][j]=''
    check=checkExists(matrix,i,j+1,word,count+1) or \
    checkExists(matrix,i+1,j,word,count+1) or \
    checkExists(matrix,i,j-1,word,count+1) or \
    checkExists(matrix,i-1,j,word,count+1)
    matrix[i][j]=temp
    return check



def wordSearch(matrix,word):
    count=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==word[count]:
                if checkExists(matrix,i,j,word,count):
                    return True
    return False

matrix=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(wordSearch(matrix,word))
