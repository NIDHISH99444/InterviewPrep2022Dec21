

def findNextGreatest(arr):
    stack,vector=[],[]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            vector.append(len(arr))
        elif arr[i]<stack[-1][0]:
            vector.append(stack[-1][1])
        elif len(stack)!=0 and arr[i]>=stack[-1][0]:
            while len(stack)!=0 and arr[i]>=stack[-1][0]:
                stack.pop()
            if len(stack)==0:
                vector.append(len(arr))
            else:
                vector.append(stack[-1][1])
        stack.append([arr[i],i])
    return vector[::-1]

arr=  [89,62,70,58,47,47,46,76,100,70]
vector=findNextGreatest(arr)
print(vector)
res=[]
for i in range(len(vector)):
    if vector[i]==len(arr):
        res.append(0)
    else:
        res.append(vector[i]-i)

print(res)







