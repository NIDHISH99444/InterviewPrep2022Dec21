def checkLength(arr,i,j):
    while i>=0 and j<len(arr) and arr[i]==arr[j]:
        i-=1
        j+=1
    return arr[i+1:j]
def longestPallindromeSubstring(arr):
    cntMax=0
    finalStr=""
    for i in range(len(arr)):
        length_str=checkLength(arr,i,i)
        if len(length_str)>cntMax:
            cntMax=len(length_str)
            finalStr=length_str
        length_str=checkLength(arr,i,i+1)
        if len(length_str)>cntMax:
            cntMax = len(length_str)
            finalStr=length_str
    return finalStr

s = "babbad"
print(longestPallindromeSubstring(s))