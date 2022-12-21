
def subarrayOfSumK( arr, k):
    sum=0
    map={0:1}
    count=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum-k in map:
            count+=map[sum-k]
        map[sum]=map.get(sum,0)+1
    return count


arr=[1,1,1]
k=2

print(subarrayOfSumK(arr,k))