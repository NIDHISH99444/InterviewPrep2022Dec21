
res=[]
def permutation(arr,index):
    if len(arr)==index:
        res.append(arr[:])
        return
    for i in range(index,len(arr)):
        arr[i],arr[index]=arr[index],arr[i]
        permutation(arr,index+1)
        arr[index], arr[i] = arr[i], arr[index]

k=5
n=3
arr=[]
for i in range(n):
    arr.append(str(i+1))
permutation(arr,0)
print(res)

