


def twoSum(nums,target):
    map={}
    for i in range(len(nums)):
        if target-nums[i] not in map:
            map[nums[i]]=i
        else:
            return map[target-nums[i]],i


nums =  [2,7,11,15]
target = 9

print(twoSum(nums,target))