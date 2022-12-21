


def findMajority(arr):
    me=arr[0]
    cnt=1
    for i in range(1,len(arr)):
        if cnt==0:
            me=arr[i]
            cnt=1
        elif arr[i]==me:
            cnt+=1
        else:
            cnt-=1
    return  me

arr=[3,2,3]
print(findMajority(arr))