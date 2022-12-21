

def pallindromeCount(arr,i,j):
    cnt=0
    while i>=0 and j<len(arr) and  arr[i]==arr[j]:
            cnt+=1
            i-=1
            j+=1

    return cnt

def pallindromeSubstring(string):
    cnt=0
    for i  in range(len(string)):
        cnt+=pallindromeCount(string,i,i)
        cnt+=pallindromeCount(string,i,i+1)
    return cnt





s = "abc"
print(pallindromeSubstring(s))