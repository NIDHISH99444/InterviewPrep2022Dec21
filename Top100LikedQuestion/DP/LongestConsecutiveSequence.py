


def maxSequence(arr):
    set_arr=set(arr)
    maxVal=0
    for ele in set_arr:
        x=ele-1
        if x not in set_arr:
            y=ele+1
            while y in  set_arr:
                y+=1
            maxVal=max(maxVal,y-x-1)

    return maxVal


arr=[102,4,100,1,101,3,2]
print(maxSequence(arr))