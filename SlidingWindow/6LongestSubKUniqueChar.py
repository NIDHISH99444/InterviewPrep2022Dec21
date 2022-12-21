

def longestSubString(arr,k):
    i,j=0,0
    map={}
    maxLen=-1
    while j<len(arr):
        if arr[j] not in map:
            map[arr[j]]=1
        else:
            map[arr[j]]+=1
        if len(map)>k:
            while len(map)>k:
                map[arr[i]]-=1
                if map[arr[i]]==0:
                    del map[arr[i]]
                i+=1
        if len(map)==k:
            maxLen=max(maxLen,j-i+1)
        j+=1
    return maxLen




arr="aabbcc"
k = 2
print(longestSubString(arr,k))