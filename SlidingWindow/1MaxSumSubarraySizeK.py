def maxSum(arr,k):
    maxVal,sum=0,0
    res=[]
    i,j,=0,0
    while j<len(arr):
        sum+=arr[j]
        if (j-i+1 ==k):
            maxVal=max(maxVal,sum)
            sum-=arr[i]
            i+=1
        j+=1
    return maxVal

arr=[2,3,5,2,9,7,1]
print(maxSum(arr,3))