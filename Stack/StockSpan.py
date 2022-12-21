

def stockSpan(arr):

    stack, vector = [], []
    for i in range(len(arr)):
        if len(stack) == 0:
            vector.append(-1)
        elif arr[i] < stack[-1][0]:
            vector.append(stack[-1][1])
        elif len(stack) != 0 and arr[i] >= stack[-1][0]:
            while len(stack) != 0 and arr[i] >= stack[-1][0]:
                stack.pop()
            if len(stack) == 0:
                vector.append(-1)
            else:
                vector.append(stack[-1][1])
        stack.append([arr[i], i])
    return vector

arr=[100,80,60,70,60,75,85]
vector=stockSpan(arr)
print(vector)
res=[]
for i in range(len(vector)):
    res.append(i-vector[i])
print(res)


