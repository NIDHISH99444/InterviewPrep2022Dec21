

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
    print(vector1)
    print(vector2)
    maxVal=0
    for i in range(len(arr)):
        maxVal=max(maxVal,(vector2[i]-vector1[i]-1)*arr[i])
    return (maxVal)

arr=[2,1,5,6,2,3]
print(histogram(arr))








