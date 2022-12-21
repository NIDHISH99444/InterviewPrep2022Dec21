
#
# def findMissingPositive(arr):
#     for i in range(len(arr)):
#         if arr[i]<=0:
#             arr[i]=0
#     for i in range(len(arr)):
#         arr[i],arr[arr[i]-1]=arr[arr[i]-1],arr[i]
#         if arr[i] < 0 or arr[i] >= len(arr):
#             continue
#     print(arr)
#     # for index,ele in enumerate(arr):
#     #     if index!=ele:
#     #         return index


def firstMissingPositive( nums):
    for i in range(len(nums)):
        while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
            tmp = nums[i]-1
            nums[i], nums[tmp] = nums[tmp], nums[i]
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1



arr= [3,4,-1,1]
# print(findMissingPositive(arr))
print(firstMissingPositive(arr))