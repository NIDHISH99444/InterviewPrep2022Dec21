def  longestRepeatingCharacterReplacement(arr,k):
    i,j=0,0
    map={}
    maxCountele=arr[0]
    maxlen=float('-inf')
    while j<len(arr):
        if arr[j] not in map:
            map[arr[j]]=1
        else:
            map[arr[j]]+=1

        if (j-i+1 - max(map.values()))>k:
            while (j - i + 1 - max(map.values())) > k:
                map[arr[i]]-=1
                if map[arr[i]]==0 :
                    del map[arr[i]]
                i+=1
        elif (j-i+1 -max(map.values()))<=k:
            maxlen=max(maxlen,j-i+1)
        j+=1

    return  maxlen

string="BAAA"
k = 0
print(longestRepeatingCharacterReplacement(string,k))