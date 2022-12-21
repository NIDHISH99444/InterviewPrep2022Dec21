def partitionLabels(arr):
    map={}
    for i in range(len(arr)):
        map[arr[i]]=i
    res,prev,maxi=[],-1,0
    for i in range(len(arr)):
        maxi=max(maxi,map[arr[i]])
        if maxi==i:
            res.append(i-prev)
            prev=maxi
    return  res



s = "eccbbbbdec"
print(partitionLabels(s))