def rotateArray(arr,k):
    # i=0
    # n=len(arr)-1
    # rem=len(arr) - k-1
    # j=rem+1
    # while i < rem:
    #     arr[i],arr[rem]=arr[rem],arr[i]
    #     i+=1
    #     rem-=1
    # while j<n:
    #     arr[j], arr[n] = arr[n], arr[j]
    #     j+=1
    #     n-=1
    # i,j=0,len(arr)-1
    # while i<j :
    #     arr[i],arr[j]=arr[j],arr[i]
    #     i+=1
    #     j-=1
    #
    # return arr

    n = len(nums)  # store length
    k %= n  # avoid unnecessary rotations
    print(nums[-k:])
    nums[:] = nums[-k:] + nums[:-k]
    return  nums

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotateArray(nums,k))