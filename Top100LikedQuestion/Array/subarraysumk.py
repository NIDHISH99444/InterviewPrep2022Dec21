



def subarraySumk(nums,k):
    sum,cnt=0,0
    map={0:1}   #important
    for i in range(len(nums)):
        sum+=nums[i]
        if (sum-k) in map:
            cnt+=map[sum-k]
        map[sum]=map.get(sum,0)+1
    return cnt




nums =  [1,2,3]
k = 3
print(subarraySumk(nums,k))

