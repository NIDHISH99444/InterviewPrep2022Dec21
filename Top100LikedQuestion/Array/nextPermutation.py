
import sys
def nextPermutation(nums):

    swap_index = sys.maxsize
    index = sys.maxsize
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            index = i - 1
            break
    if index == sys.maxsize:
        nums.reverse()
        return nums
    for j in range(len(nums) - 1, index - 1, -1):
        if nums[j] > nums[index]:
            # if nums[j] < res:
            #     res = nums[j]
            swap_index = j
            break
    nums[swap_index], nums[index] = nums[index], nums[swap_index]
    nums[index + 1:] = sorted(nums[index + 1:])
    return nums


nums = [1,3,2]
print(nextPermutation(nums))

