


def findMinRotatedSorted(arr):
    low,high=0,len(arr)-1
    n=len(arr)-1
    if arr[low]<arr[high]:
        return arr[low]
    while low<=high:
        mid=low+(high-low)//2
        prev=(mid-1)%n
        next=(mid+n-1)%n
        if arr[mid]<arr[prev] and arr[mid]<arr[next]:
            return arr[mid]
        elif arr[mid]>=arr[0]:
            low=mid+1
        else:
            high=mid-1



nums = [5,1,2,3,4]
print(findMinRotatedSorted(nums))