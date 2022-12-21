

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
    return  maxLen


# k = 2
# print(longestSubString(arr,k))

def longestSubstringWithoutRepeatingChar(arr):
    i,j=0,0
    map={}
    maxLen=-1
    while j<len(arr):
        if arr[j] not in map:
            map[arr[j]]=1
        else:
            map[arr[j]]+=1
        if len(map)<j-i+1:
            while len(map)<j-i+1:
                map[arr[i]]-=1
                if map[arr[i]]==0:
                    del map[arr[i]]
                i+=1
        if len(map)==j-i+1:
            maxLen=max(maxLen,j-i+1)
        j+=1
    return  maxLen

import sys
def minWinSubstring(s,t):
    map={}
    minLen=sys.maxsize
    for ele in t :
        if ele not in map:
            map[ele]=1
        else:
            map[ele]+=1
    cnt=len(map)
    i,j=0,0
    ini=-1
    while j<len(s):
        if s[j] in map:
            map[s[j]]-=1
            if map[s[j]]==0:
                cnt-=1
        while cnt==0:
            if j-i+1 < minLen:
                minLen=(j-i+1)
                ini=i
                fin=j
            if s[i] in map:
                map[s[i]]+=1
                if map[s[i]]==1:
                    cnt+=1
            i+=1
        j+=1
    if ini!=-1:
        return (s[ini:fin+1])
    else:
        return ""


# arr="aabbcc"
# print(longestSubstringWithoutRepeatingChar(arr))

s = 'a'
t = 'a'
print(minWinSubstring(s, t))