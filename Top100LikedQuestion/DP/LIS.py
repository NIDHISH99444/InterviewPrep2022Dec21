


def jumpgame(nums):
    l = r = 0
    nJumps = 0
    while r < len(nums) - 1:
        nJumps += 1
        furthest = max([i + nums[i] for i in range(l, r + 1)])
        l, r = r + 1, furthest

    return nJumps


nums = [2,3,1,1,4]
print(jumpgame(nums))