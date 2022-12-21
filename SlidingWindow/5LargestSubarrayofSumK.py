
def subarrayOfSumK( arr, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """


    sum = 0
    map = {0: -1}

    maxlen=0
    for i in range(len(arr)):
        sum += arr[i]
        if sum - k in map:

            if i-map[sum-k] > maxlen:
                maxlen=i-map[sum-k]
                print(map[sum - k]+1,i)

        map[sum] = i
    return maxlen


arr=[2,3,3,-1,0,7,-2,5]
k=5

print(subarrayOfSumK(arr,k))