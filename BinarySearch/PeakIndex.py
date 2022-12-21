
def peak(arr):
    low =0
    high =len(arr) -1
    if len(arr)==1:
        return 0
    while low<=high:
        mid =(low +(high -low )//2)
        if mid >0 and mid <len(arr) -1 :
            if  arr[mid] >arr[mid-1] and arr[mid] >arr[mid+1]:
                return mid
            elif arr[mid] <arr[mid -1]:
                high =mid -1
            else:
                low =mid +1
        if mid==0:
            if arr[mid] >arr[mid+1]:
                return mid
            else:
                return mid +1

        if mid==len(arr) -1:
            if arr[mid] >arr[mid-1]:
                return mid
            else:
                return mid -1

print(peak([1]))





