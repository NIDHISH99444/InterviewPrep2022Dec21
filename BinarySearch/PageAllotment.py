def isValid(nums,mid,k):
    counter,sum=0,0
    for i in range(len(nums)):
        sum+=nums[i]
        if sum > mid:
            counter+=1
            sum=nums[i]
    return counter < k


def allotmentPages(nums,k):
    res=-1
    start=max(nums)
    end=sum(nums)
    while start <= end :
        mid=(start+end)//2
        if isValid(nums,mid,k):
            res=mid
            end=mid-1
            print(end)
        else:
            start=mid+1
    return  res


nums = [12, 34, 67, 90]
nums = [10, 20, 30, 40]
k=2
print(allotmentPages(nums,k))
