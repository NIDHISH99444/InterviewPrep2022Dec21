import sys



def findMaxProd(arr):
    l,r=1,1
    maxProd = arr[0]
    for i in range(len(arr)):
        if l == 0:
            l=1

        l*=arr[i]
        maxProd=max(maxProd,l)


    for i in range(len(arr)-1,-1,-1):
        if r == 0:
            r=1
        r*=arr[i]
        maxProd = max(maxProd, r)

    return maxProd

arr=[-2,-3,-5]
print(findMaxProd(arr))

