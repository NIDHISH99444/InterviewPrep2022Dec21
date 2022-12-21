
def findFittingLocation(ele,res):
    low=0
    high=len(res)-1
    val=0
    while low<=high:
        mid=low+(high-low)//2
        if res[mid]>=ele:
            val = mid
            high = mid - 1
        elif res[mid]<ele:
            low=mid+1
    return  val


def findLIS(nums):
    res=[nums[0]]
    for i in range(1,len(nums)):
        if nums[i]>res[-1]:
            res.append(nums[i])
        else:
            loc=findFittingLocation(nums[i],res)
            res[loc]=nums[i]
    return res




nums = [3,5,6,2,5,4,19,5,6,7,12]
print(findLIS(nums))

