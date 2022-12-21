


def jumpGame(arr):
    finalReachable=0
    for i in range(len(arr)):
        if i>finalReachable:
            return False
        maxjump=arr[i]+i
        finalReachable=max(finalReachable,maxjump)
    return finalReachable>=len(arr)-1




nums = [2,3,1,1,4]
print(jumpGame(nums))