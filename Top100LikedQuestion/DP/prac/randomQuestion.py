
def longestSubsequence(arr):
    set_arr=set(arr)
    maxLen=float('-inf')
    for ele in set_arr:
        x=ele-1
        if x not in set_arr:
            y=ele+1
            while y in set_arr:
                y+=1
            maxLen=max(maxLen,y-x-1)
    return maxLen



arr=[2,1,4,3,101,102]
# print(longestSubsequence(arr))
