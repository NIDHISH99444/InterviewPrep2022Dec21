nums = [5,7,7,8,8,10]
target = 8


def firstPos(arr,target):
    low =0
    high =len(arr) -1
    if len(arr)==1:
        return 0
    res=-1
    while low<=high:
        mid =(low +(high -low )//2)
        if arr[mid]==target:
            res=mid
            high=mid-1
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1

    return res


def LastPos(arr,target):
    low =0
    high =len(arr) -1
    if len(arr)==1:
        return 0
    res=-1
    while low<=high:
        mid =(low +(high -low )//2)
        if arr[mid]==target:
            res=mid
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return res


print(firstPos(nums,target))
print(LastPos(nums,target))
