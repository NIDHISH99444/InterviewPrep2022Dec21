weights =[3,2,2,4,1,4]
days = 3

def checkCapacity(weight,mid,days):

    sum,cnt=0,1
    for i in range(len(weight)):
        sum+=weight[i]
        if sum > mid:
            sum=weight[i]
            cnt+=1
    if cnt<=days:
        return True
    return  False

def capacity(weight,days):

    low=max(weights)
    high=sum(weight)
    while low<=high:
        mid=low+(high-low)//2
        res=checkCapacity(weight,mid,days)
        if res ==True:
            newres=mid
            high=mid-1
        else:
            low=mid+1
    return newres


print(capacity(weights,days))
#
# def shipWithinDays( weights, D):
#     def helper(target, D):
#         cnt = 0
#         cur = 0
#         for w in weights:
#             if cur + w > mid:
#                 cnt += 1
#                 cur = 0
#             cur += w
#         return cnt >= D
#
#
#     left, right = max(weights), sum(weights)
#
#     while left <= right:
#         mid = (left + right) // 2
#         if helper(mid, D):
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return left
#
# print(shipWithinDays(weights,days))