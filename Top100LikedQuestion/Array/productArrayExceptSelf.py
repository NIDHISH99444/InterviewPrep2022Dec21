


def product(nums):
    right=[1]*len(nums)
    left=[1]*len(nums)
    for i in range(len(nums)-1,0,-1):
        right[i-1]=right[i]*nums[i]
    for i in range(1,len(nums)):
        left[i]=left[i-1]*nums[i-1]
    print(right)
    print(left)
    res=[]
    for i in range(len(nums)):
        res.append(left[i]*right[i])
    print(res)



nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
product(nums)
