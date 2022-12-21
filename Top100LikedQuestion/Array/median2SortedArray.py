import sys
def medianArray(arr1,arr2):

    if len(arr1)> len(arr2) :
        return medianArray(arr2,arr1)
    low = 0
    high = len(arr1)
    while low<=high:
        cnt1 = (low+high) // 2
        cnt2=(len(arr1)+len(arr2)+1)//2 - cnt1
        if cnt1==0:
            l1=-sys.maxsize
        else:
            l1=arr1[cnt1-1]
        if cnt2==0:
            l2 = -sys.maxsize
        else:
            l2 = arr2[cnt2-1]
        if cnt1==len(arr1):
            r1=sys.maxsize
        else:
            r1=arr1[cnt1]
        if cnt2==len(arr2):
            r2 = sys.maxsize
        else:
            r2 = arr2[cnt2]
        if l1<=r2 and l2<=r1:
            if (len(arr1)+len(arr2))%2==0:
                return (max(l1,l2)+min(r1,r2))/2.0
            else:
                return max(l1,l2)
        elif l2>r1:
            low = cnt1 +1
        elif l1>r2:
            high= cnt1 -1



a=[5]
b=[]

print(medianArray(a,b))