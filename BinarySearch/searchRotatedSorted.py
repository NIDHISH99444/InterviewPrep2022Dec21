
def  rotatedSorted(arr):
    n=len(arr)
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+(high-low)//2)
        next=(mid+1)%n
        prev=(mid+n-1)%n
        if arr[mid]<arr[prev] and arr[mid]<arr[next]:
            return mid
        elif arr[mid]>=arr[0]:
            low=mid+1
        else:
            high=mid-1

def bs(arr,low,high):

    while low<=high:
        mid = low + (high - low) // 2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1

def find(nums,target):
    index = rotatedSorted(nums)
    print("index",index)
    res = -1
    if len(nums) == 1 and nums[0] == target:
        return 0

    res1=bs(nums, 0, index - 1)
    res2=bs(nums, index, len(nums) - 1)
    if res1 ==None and res2==None:
        return -1
    else:
        return res1 or res2
    # return (bs(nums, 0, index - 1)) or bs(nums, index, len(nums) - 1) or res

nums = [4,5,6,7,0,1,2]
target = 0
print(find(nums,target))




