def  firstNegNoWindowSizeK(arr,k):
    i,j,=0,0
    lst,res=[],[]
    while j<len(arr):
        if arr[j]<0:
            lst.append(arr[j])
        if j-i+1 == k :
            if len(lst):
                res.append(lst[0])
                if arr[i]==lst[0]:
                    lst.pop(0)
            else:
                res.append(0)
            i+=1
        j+=1
    return res


arr=[12,-1,-7,8,-15,30,16,28]
print(firstNegNoWindowSizeK(arr,3))