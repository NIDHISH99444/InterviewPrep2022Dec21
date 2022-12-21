# res=[]
# def generate(open,close,n,str):
#     if len(str)==(2*n):
#         res.append(str)
#         return
#     if open<n:
#         generate(open+1,close,n,str+'(')
#     if close<open:
#         generate(open,close+1,n,str+')')
#
# str=""
# open,close=0,0
# n=3
# # generate(open,close,n,str)
# # print(res)
#
# res=[]
# def permutation(index,nums):
#     if index==len(nums):
#         res.append(nums[:])
#         return
#     for i in range(index,len(nums)):
#         nums[index],nums[i]=nums[i],nums[index]
#         permutation(i+1,nums)
#         nums[index], nums[i] = nums[i], nums[index]
#
#
# nums = [1,2,3]
# # permutation(0,nums)
# # print(res)
# res=[]
# def combinationSum(index,nums,target,ds):
#     if target==0:
#         print(ds)
#         res.append(ds)
#         return res
#     if index<0:
#         return []
#
#     take=[]
#     if nums[index]<=target:
#         take=combinationSum(index,nums,target-nums[index],ds+[nums[index]])
#     notTake=combinationSum(index-1,nums,target,ds)
#
#     return take+notTake
#
# #
# # candidates = [2,3]
# # target = 8
# # t=[[-1 for i in range(target+1)]for j in range(len(candidates)+1) ]
# # # combinationSum(len(candidates)-1,candidates,target,[])
# # # print(res)
# #
# # def group(strs):
# #     map={}
# #     for ele in strs:
# #         key="".join(sorted(ele))
# #         print(key)
# #         if  key not in map:
# #             map[key]=[ele]
# #         else:
# #             map[key].append(ele)
# #     res=[]
# #     for val in map.values():
# #         res.append(val)
# #     print(res)
# #
# # # strs = ["eat","tea","tan","ate","nat","bat"]
# # # group(strs)
# #
# # from heapq import  heappop,heappush
# #
# # def kthLargest(nums,k):
# #     heap=[]
# #     for i in range(len(nums)):
# #         heappush(heap,nums[i])
# #         if len(heap)>k:
# #             heappop(heap)
# #     return heap[0]
# #
# #
# #
# #
# # nums = [3,2,1,5,6,4]
# # # k = 2
# # # print(kthLargest(nums,k))
# #
# #
# # def topK(nums,k):
# #     map={}
# #     for i in range(len(nums)):
# #         nums[i]
# # nums = [1, 1, 1, 2, 2, 3]
# #
# # k = 2
# # topK(nums,k)
#
#
# def mergeInterval(intervals):
#     intervals.sort(key=lambda x:x[0])
#     res=[]
#     res.append(intervals[0])
#     for i in range(1,len(intervals)):
#         if intervals[i][0]>res[-1][1]:
#             res.append(intervals[i])
#         else:
#             last=res.pop()
#
#             res.append([last[0],max(last[1],intervals[i][1])])
#     return (res)
#
#
#
# s=[[1,6],[2,4],[8,10],[15,18]]
#
# print(mergeInterval(s))
#
#
# def nonOverlappingInterval(interval):
#     interval.sort(key=lambda x : x[1])
#     end=float('-inf')
#     cnt=0
#     for s,e in interval:
#         if s>=end:
#             end=e
#         else:
#             cnt+=1
#     return  cnt
#
#
#
# interval=[[1,2],[2,3],[3,4],[1,3]]
# print(nonOverlappingInterval(interval))
#
#
# def maximumMeetings( start, end):
#
#     nums, cnt = [], 0
#     for i in range(len(start)):
#         nums.append((start[i], end[i]))
#     print(nums)
#     finalend = float('-inf')
#     nums.sort(key=lambda n: n[1])
#
#     for s, e in nums:
#         if s > finalend:
#             finalend = e
#             cnt += 1
#
#     return cnt
#
#
# start = [1,3,0,5,8,5]
# end =  [2,4,6,7,9,9]
#
# # print(maximumMeetings(start,end))
#
# def maxMeetingRoomRequired(intervals):
#     first,sec=[],[]
#     for ele in intervals:
#         first.append(ele[0])
#         sec.append(ele[1])
#     cnt=0
#     first.sort()
#     sec.sort()
#     maxCnt=float('-inf')
#     i,j=0,0
#     while i<len(first):
#         if first[i]<=sec[j]:
#             cnt+=1
#             maxCnt=max(maxCnt,cnt)
#             i+=1
#         else:
#             cnt-=1
#             j+=1
#     return maxCnt
#
#
#
# interval=[(0,30),(5,10),(15,20)]
# print(maxMeetingRoomRequired(interval))
#
#
# def search():
#     pass
#
#
# def peak(arr):
#     low,high=0,len(arr)-1
#     n=len(arr)
#     while low<=high:
#         mid=low+(high-low)//2
#         prev=(n+mid-1)%n
#         next=(mid+1)%n
#         if arr[mid]>arr[prev] and arr[mid]>arr[next]:
#             return mid
#         elif arr[mid]>arr[0]:
#             low=mid+1
#         else:
#             high=mid-1
#
# def find(arr,low,high,ele):
#     while low <= high:
#         mid = low + (high - low) // 2
#         if arr[mid]==ele:
#             return mid
#         elif arr[mid]>ele:
#             high=mid-1
#         else:
#             low=mid+1
#     return  -1
#
#
# arr=[4,5,6,7,0,1,2,3]
# index=peak(arr)
# ele=0
# print(find(arr,0,index,ele))
# print(find(arr,index+1,len(arr),ele))
#
#
# def findRepeated(nums):
#
#     for i in range(len(nums)):
#         if nums[abs(nums[i])-1] < 0:
#             return abs(nums[i])
#         else:
#             nums[abs(nums[i]) - 1]=-nums[abs(nums[i])-1]
#
#
#
#
# nums = [3,1,3,4,2]
# print(findRepeated(nums))
#
#
#
# def findMinPeak(arr):
#     low,high=0,len(arr)-1
#     n=len(arr)
#     while low<=high:
#         mid=low+(high-low)//2
#         prev=(n+mid-1)%n
#         next=(mid+1)%n
#         if arr[mid]<arr[prev] and arr[mid]<arr[next]:
#             return arr[mid]
#         elif arr[mid]>=arr[0]:
#             low=mid+1
#         else:
#             high=mid-1
#
# arr=[2,1]
# print(findMinPeak(arr))
#
#
# def search(arr,target):
#     i=0
#     j=len(arr[0])-1
#     while i<len(arr) and j>=0:
#         if arr[i][j]>target:
#             j-=1
#         elif arr[i][j]<target:
#             i+=1
#         else:
#             return True
#     return False
#
#
# arr=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 5
# print(search(arr,target))
#
# def findLow(arr,ele):
#     low=0
#     high=len(arr)-1
#     index=-1
#     while low<=high:
#         mid=low+(high-low)//2
#         if arr[mid]==ele:
#             index=mid
#             high=mid-1
#         elif arr[mid]>ele:
#             high=mid-1
#         else:
#             low=mid+1
#     return index
#
#
# nums = [5,7,7,8,8,10]
# target = 8
# print(findLow(nums,target))
#
# def findIndex(arr,ele):
#     low=0
#     high=len(arr)-1
#     index=-1
#     while low<=high:
#         mid=low+(high-low)//2
#         if arr[mid]>=ele:
#             index=mid
#             high=mid-1
#         else:
#             low=mid+1
#     return index
#
# def findLongest(arr):
#     res=[]
#     res.append(arr[0])
#     for i in range(1,len(arr)):
#         if arr[i]>res[-1]:
#             res.append(arr[i])
#         else:
#             index=findIndex(res,arr[i])
#             res[index]=arr[i]
#     print(res)
#     return len(res)
#
# lis=[10,9,2,5,3,7,101,18]
# print(findLongest(lis))
#
# def dailytemp(arr):
#     stack=[]
#     res=[]
#     for i in range(len(arr)-1,-1,-1):
#         if not len(stack):
#             res.append(0)
#         elif len(stack) and arr[i]<stack[-1][0]:
#             res.append(stack[-1][1]-i)
#         elif len(stack) and arr[i]>=stack[-1][0]:
#             while len(stack) and arr[i]>=stack[-1][0]:
#                 stack.pop()
#             if len(stack):
#                 res.append(stack[-1][1]-i)
#             else:
#                 res.append(0)
#         stack.append([arr[i], i])
#     print(res)
#     return res[::-1]
#
#
#
# temperatures =[89,62,70,58,47,47,46,76,100,70]
# print(dailytemp(temperatures))
#
#
# def longestSubstring(arr):
#     i,j=0,0
#     map={}
#     maxLen=0
#     while j<len(arr):
#         if arr[j] not in map:
#             map[arr[j]]=1
#         else:
#             map[arr[j]]+=1
#         while j-i+1 > len(map):
#             map[arr[i]]-=1
#             if map[arr[i]]==0:
#                 del map[arr[i]]
#             i+=1
#         if j-i+1==len(map):
#             maxLen=max(maxLen,j-i+1)
#         j+=1
#
#     return maxLen
# s = "pwwkew"
# print(longestSubstring(s))
#
#
# def findAllAna(s,p):
#     map={}
#     for ele in p:
#         if ele not in map:
#             map[ele]=1
#         else:
#             map[ele]+=1
#     i,j=0,0
#     cnt=len(map)
#     res=[]
#     while j<len(s):
#         if s[j] in map:
#             map[s[j]]-=1
#             if map[s[j]]==0:
#                 cnt-=1
#         while j-i+1 >len(p):
#             if s[i] in map:
#                 map[s[i]]+=1
#                 if map[s[i]]==1:
#                     cnt+=1
#             i+=1
#         if j-i+1==len(p) and cnt==0:
#             res.append(i)
#         j+=1
#
#     return res
# s = "abab"
# p = "ab"
# print(findAllAna(s,p))
# from heapq import  heappop,heappush
# def topkelement(nums,k):
#     map={}
#     heap=[]
#     for ele in nums:
#         map[ele]=map.get(ele,0)+1
#     for key,val in map.items():
#         heappush(heap,(-val,key))
#     res=[]
#     while k>0:
#         key,val=heappop(heap)
#         res.append(val)
#         k-=1
#     return res
#
# nums = [1,1,1,2,2,3]
# k = 2
# print(topkelement(nums,k))
#
#
# def lcs(string1,string2,n,m):
#     if n<0 or m<0 :
#         return ""
#
#     if string1[n]==string2[m]:
#         return string1[n]+lcs(string1,string2,n-1,m-1)
#     else:
#         left=lcs(string1,string2,n-1,m)
#         right=lcs(string1,string2,n,m-1)
#         if  len(left)>len(right):
#             return left
#         else:
#             return right
#
#
# text1 = "cbbd"
# text2=text1[::-1]
# n=len(text1)-1
# m=len(text2)-1
#
# dp=[[-1 for i in range(m+1)] for j in range(n+1)]
# print("lcs",lcs(text1,text2,n,m))

#
#
# def uniquePath(dp,i,j):
#     if i<0 or j<0:
#         return 0
#     if i==0 and j==0:
#         return 1
#     if dp[i][j]!=-1:
#         return dp[i][j]
#     up=uniquePath(dp,i-1,j)
#     left=uniquePath(dp,i,j-1)
#     dp[i][j]=up+left
#     return dp[i][j]
#
#
# m = 3
# n = 7
# dp=[[-1 for i in range(n)] for j in range(m)]
# print(uniquePath(dp,m-1,n-1))
#
# def findMinPathSum(grid,i,j,dp):
#     if i<0 or j<0:
#         return float('inf')
#     if i==0 and j==0:
#         return grid[i][j]
#     if dp[i][j]!=-1:
#         return dp[i][j]
#     up=findMinPathSum(grid,i-1,j,dp)
#     left=findMinPathSum(grid,i,j-1,dp)
#     dp[i][j]= min(up,left)+grid[i][j]
#     return dp[i][j]
#
#
#
#
# grid = [[1,3,1],[1,5,1],[4,2,1]]
# dp=[[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
# print(findMinPathSum(grid,len(grid)-1,len(grid[0])-1,dp))
#
#
#
# def maxSubarray(arr):
#     msf,meh=0,0
#     for ele in arr:
#         msf+=ele
#         meh=max(meh,msf)
#         if msf<0:
#             msf=0
#     return meh
#
#
#
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubarray(nums))

# def houseRobbery(arr,index,dp):
#     if index<0:
#         return 0
#     if dp[index]!=-1:
#         return dp[index]
#     take=arr[index]+houseRobbery(arr,index-2,dp)
#     notTake=houseRobbery(arr,index-1,dp)
#     dp[index]=max(take,notTake)
#     return dp[index]
#
#
# nums = [2,7,9,3,1]
# dp=[-1 for i in range(len(nums))]
# print(houseRobbery(nums,len(nums)-1,dp))
#

# def partition(arr,index,target):
#     if target == 0:
#         return True
#     if index<0:
#         return False
#
#     if dp[index][target]!=-1:
#         return dp[index][target]
#     take=False
#     if target>=arr[index]:
#         take=partition(arr,index-1,target-arr[index])
#     notTake=partition(arr,index-1,target)
#     dp[index][target]= take or notTake
#     return  dp[index][target]
#
#
# nums=[1,5,5]
# target=11
# dp=[[-1 for i in range(target+1)]for j in range(len(nums))]
# print(partition(nums,len(nums)-1,target))



# def jumpGame(arr,start):
#     if start>=len(arr)-1:
#         return 0
#     if dp[start]!=-1:
#         return dp[start]
#     minJumps=float("inf")
#     for i in range(start+1,start+arr[start]+1):
#         minJumps=min(minJumps,1+jumpGame(arr,i))
#     dp[start]= minJumps
#     return dp[start]
#
#
#
#
#
# arr=[2,2,0,0,4]
# dp=[-1]*len(arr)
# print(jumpGame(arr,0))


def nextPermutation(arr):
    index,swapIndex=float('inf'),float('inf')
    for i in range(len(arr)-1,0,-1):
        if arr[i]>arr[i-1]:
            index=i-1
            break
    if index==float('inf'):
        return sorted(arr)
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>arr[index]:
            swapIndex=i
            break
    arr[index],arr[swapIndex]=arr[swapIndex],arr[index]
    return (arr[:index+1]+sorted(arr[index+1:]))


arr=[1,2,3]
print(nextPermutation(arr))

def check(arr,i,j):
    while i>=0 and j<len(arr) and arr[i]==arr[j]:
        i-=1
        j+=1
    return arr[i+1:j]

def longestPallindrome(arr):
    maxLen=float("-inf")
    finalString=''
    for i in range(len(arr)):
        cs=check(arr,i,i)

        if len(cs)>maxLen:
            maxLen=len(cs)
            finalString=cs
        cs=check(arr,i,i+1)

        if len(cs)>maxLen:
            maxLen=len(cs)
            finalString=cs
    return finalString



string="babad"
print(longestPallindrome(string))




def wordBreak( s: str, wordDict):

    q = [s]
    seen = set()
    while q:
        s = q.pop(0)    # popleft() = BFS ; pop() = DFS
        for word in wordDict:
            if s.startswith(word):
                new_s = s[len(word):]
                if new_s == "":
                    return True
                if new_s not in seen:
                    q.append(new_s)
                    seen.add(new_s)
    return False


s = "aab"
wordDict = ['aaa','aa','ab']
print(wordBreak(s,wordDict))

# def threesum(arr):
#     res=[]
#     arr.sort()
#     previ=float('inf')
#     for i in range(len(arr)-2):
#         if arr[i]==previ:
#             continue
#         else:
#             previ=arr[i]
#         j=i+1
#         k=len(arr)-1
#
#         while j<k:
#             prevj, prevk = j, k
#             if arr[i]+arr[j]+arr[k]==0:
#                 res.append([arr[i],arr[j],arr[k]])
#                 while j < k and arr[prevk] == arr[k]:
#                     k -= 1
#                 while j < k and arr[prevj] == arr[j]:
#                     j+=1
#             elif arr[i]+arr[j]+arr[k]>0:
#                 k-=1
#             else:
#                 j+=1
#
#     return(res)
#
#
# nums = [-4,-1,-1,0,1,2]
# print(threesum(nums))
#
# def subArray(index,target):
#
#
# nums = [1,2,3]
# k = 3

def subarraySum(arr,k):
    map={0:1}
    cnt=0
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum-k in map:
            cnt+=map[sum-k]
        map[sum]=map.get(sum,0)+1
    return cnt

arr=[1,2,3]
print(subarraySum(arr,3))


def iterate(matrix,i,j,word,counter):
    if counter==len(word):
        return True
    if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]!=word[counter]:
        return False

    temp=matrix[i][j]
    matrix[i][j]=''
    chosen=iterate(matrix,i-1,j,word,counter+1) or \
    iterate(matrix, i, j+1, word, counter + 1) or \
    iterate(matrix, i+1, j, word, counter + 1) or \
    iterate(matrix, i, j-1, word, counter + 1)
    matrix[i][j]=temp
    return chosen

def wordSearch(matrix,word):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==word[0]:
                if iterate(matrix,i,j,word,0):
                    return True
    return False




matrix=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]      
word = "ABCCED"
cnt=len(word)
print(wordSearch(matrix,word))
