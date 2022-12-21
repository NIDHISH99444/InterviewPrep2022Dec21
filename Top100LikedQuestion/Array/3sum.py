


def threeSum(arr):
    prev=None
    res=[]
    arr.sort()
    for i in range(len(arr)):
        if prev==arr[i]:
            continue
        prev=first=arr[i]
        sum=-arr[i]
        j,k=i+1,len(arr)-1
        while j<k:
            if arr[j]+arr[k] ==sum:
                res.append([first,arr[j],arr[k]])
                prevj,prevk=arr[j],arr[k]
                while j<k and arr[j]==prevj:
                        j+=1
                while j<k and arr[k]==prevk:
                        k-=1
            elif arr[j]+arr[k]<sum:
                j+=1
            else:
                k-=1

    return res





arr=[-1,0,1]
print(threeSum(arr))