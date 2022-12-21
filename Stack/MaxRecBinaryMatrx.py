

def nextSmallestLeft(arr):
    stack,vector=[],[]
    for i in range(len(arr)):
        if len(stack)==0:
            vector.append(-1)
        elif arr[i]>stack[-1][0]:
            vector.append(stack[-1][1])
        elif len(stack)!=0 and arr[i]<=stack[-1][0]:
            while len(stack)!=0 and arr[i]<=stack[-1][0]:
                stack.pop()
            if len(stack)==0:
                vector.append(-1)
            else:
                vector.append(stack[-1][1])
        stack.append([arr[i],i])
    return vector

def nextSmallestRight(arr):
    stack, vector = [], []
    for i in range(len(arr)-1,-1,-1):
        if len(stack) == 0:
            vector.append(len(arr))
        elif arr[i] > stack[-1][0]:
            vector.append(stack[-1][1])
        elif len(stack) != 0 and arr[i] <= stack[-1][0]:
            while len(stack) != 0 and arr[i] <= stack[-1][0]:
                stack.pop()
            if len(stack) == 0:
                vector.append(len(arr))
            else:
                vector.append(stack[-1][1])
        stack.append([arr[i], i])
    return vector[::-1]





def histogram(arr):
    vector1 = nextSmallestLeft(arr)
    vector2 = nextSmallestRight(arr)
    maxVal=0
    for i in range(len(arr)):
        maxVal=max(maxVal,(vector2[i]-vector1[i]-1)*arr[i])
    return (maxVal)

modMatrix=[]
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
for i in range(len(matrix)):
    res = []
    for j in range(len(matrix[0])):
        if matrix[i][j]=='0':
            res.append(0)
        else:
            res.append(1)

    modMatrix.append(res)


def largestArea(modMatrix):
    finalMax=0
    vector = [0] * len(modMatrix[0])
    for i in range(len(modMatrix)):

        for j in range(len(modMatrix[0])):
            if modMatrix[i][j]==1:
                vector[j]+=modMatrix[i][j]
            else:
                vector[j]=0
        print(vector)
        finalMax=max(finalMax,histogram(vector))
    return  finalMax

print(largestArea(modMatrix))










