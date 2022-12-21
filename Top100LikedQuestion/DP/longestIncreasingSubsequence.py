

def lis(nums):
    res=[1]*len(nums)
    for i in range(len(nums)):
        j=0
        while j<i:
            if nums[j]<=nums[i]:
                res[i]=max(res[i],res[j]+1)
            j+=1
    return max(res)



nums = [1,3,6,7,9,4,10,5,6]

print(lis(nums))