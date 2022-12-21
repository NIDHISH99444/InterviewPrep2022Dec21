def maxSubarray(arr):
    msf,maxsum=0,arr[0]
    for i in range(len(arr)):
        msf+=arr[i]
        maxsum=max(maxsum,msf)
        if msf<0:
            msf=0
    return maxsum


arr= [1]
print(maxSubarray(arr))