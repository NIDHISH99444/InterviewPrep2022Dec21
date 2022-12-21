def singleNumber(arr):
    res=0
    for i in range(len(arr)):
        res^=arr[i]
    return res




nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))