def canPartition( nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    def subsetSum(a, index, target):
        if target == 0:
            return True
        if index < 0:
            return False
        if index == 0:
            if a[index] == target:
                return True
        if tab[index][target] != -1:
            return tab[index][target]
        nottake = subsetSum(a, index - 1, target)
        take = False
        if a[index] <= target:
            take = subsetSum(a, index - 1, target - a[index])

        tab[index][target] = take or nottake
        return tab[index][target]



    if sum(nums) % 2 != 0:
        return (False)
    else:
        k = sum(nums) // 2
        n = len(nums) - 1
        tab = [[-1 for i in range(k+1)] for j in range(n+1)]
        return (subsetSum(nums, n, k))



print(canPartition([100,100,100,100,100,100,100,100]))
