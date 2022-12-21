

def maxAreaCalc(arr):
    maxArea=0
    i,j=0,len(arr)-1
    while i<=j:
        if arr[i]<arr[j]:
            maxArea=max(maxArea,(j-i)*arr[i])
            i+=1
        else:
            maxArea = max(maxArea, (j - i) * arr[j])
            j -= 1
    return maxArea

height=[1,8,6,2,5,4,8,3,7]
print(maxAreaCalc(height))
