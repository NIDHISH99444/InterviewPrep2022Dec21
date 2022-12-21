
import  sys
def isPallindrome(arr,i,j):
    while i<=j:
        if arr[i]!=arr[j]:
            return False
        i+=1
        j-=1
    return  True

def pallindromePartition(arr,i,j,t):
    if i>=j:
        return 0
    if isPallindrome(arr,i,j):
        return 0
    if t[i][j]!=-1:
        return  t[i][j]
    minVal=sys.maxsize
    for k in range(i,j):
        temp=pallindromePartition(arr,i,k,t)+pallindromePartition(arr,k+1,j,t)+1
        minVal=min(minVal,temp)
    t[i][j]=minVal
    return minVal


s = "nitik"
t = [[-1 for i in range(len(s))]for j in range(len(s))]
print(t)
print(pallindromePartition(s,0,len(s)-1,t))