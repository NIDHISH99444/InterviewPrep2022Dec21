

def findNextGreatest(arr):
    stack,vector=[],[]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            vector.append(-1)
        elif arr[i]<stack[-1]:
            vector.append(stack[-1])
        elif len(stack)!=0 and arr[i]>stack[-1]:
            while len(stack)!=0 and arr[i]>stack[-1]:
                stack.pop()
            if len(stack)==0:
                vector.append(-1)
            else:
                vector.append(stack[-1])
        stack.append(arr[i])

    return vector[::-1]

arr=[1,3,4,2]
vector=findNextGreatest(arr)
dict={}
for i in range(len(arr)):
    dict[arr[i]]=vector[i]

print(dict)

nums1 = [4,1,2]
res=[]
for ele in nums1:
    res.append(dict[ele])
print(res)



