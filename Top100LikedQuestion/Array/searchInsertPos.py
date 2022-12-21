def searchPos(arr,target):
    low,high=0,len(arr)-1
    res=len(arr)
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            res=mid
            high=high-1
        else:
            low=low+1
    return res








nums = [1, 3, 5, 6]
target = 0
print(searchPos(nums,target))