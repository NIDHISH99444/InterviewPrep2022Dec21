

def merge( intervals,newinterval):
    intervals.append(newinterval)
    intervals.sort()

    res=[intervals[0]]
    for i in range(1,len(intervals)):
        if res[-1][1]>=intervals[i][0]:
            newres=[res[-1][0],max(res[-1][1],intervals[i][1])]
            res.pop()
            res.append(newres)
        else:
            res.append(intervals[i])
    return (res)


def meeting1(nums):
    finalend=float('-inf')
    nums.sort(key=lambda n : n[1])

    for start, end in nums:
        if start>=finalend:
            finalend=end
        else:
            return False

    return True



def maximumMeeting(start,end):
    nums,cnt = [],0
    for i in range(len(start)):
        nums.append((start[i], end[i]))
    print(nums)
    finalend = float('-inf')
    nums.sort(key=lambda n: n[1])

    for s, e in nums:
        if s > finalend:
            finalend = e
            cnt+=1

    return cnt
def nonOverlapping( intervals):

    intervals.sort(key=lambda x:x [1])
    end=float('-inf')
    cnt=0
    for s,e in intervals:
        if s>=end:
            end=e
        else:
            cnt+=1
    return cnt

#
# intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
intervals =[[1,2],[2,3],[1,3],[3,4]]

print(nonOverlapping(intervals))
#
# nums=[(0,30),(5,10),(15,20)]
# print(meeting1(nums))
N = 6
start = [1,3,0,5,8,5]
end =  [2,4,6,7,9,9]
print(maximumMeeting(start,end))
