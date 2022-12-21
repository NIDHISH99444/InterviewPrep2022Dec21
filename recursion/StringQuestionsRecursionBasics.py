

#print all substring

def subset(chosen,remainder):
    if len(remainder) ==0:
        print(chosen)
        return
    subset(chosen+remainder[0],remainder[1:])
    subset(chosen,remainder[1:])
#subset('',"abc")

#returing list without passing res variable
def subsetListReturn(chosen,remainder):
    if len(remainder) ==0:
        res=[]
        res.append(chosen)
        return res
    left=subsetListReturn(chosen+remainder[0],remainder[1:])
    right=subsetListReturn(chosen,remainder[1:])
    left.extend(right)
    return left
# print("subset list ",subsetListReturn('',"abc"))


def checksum(chosen,remainder,expectedsum):
    if len(remainder)==0:
        res=[]
        if sum(chosen)==expectedsum:
            res.append(chosen)
        return res
    return checksum(chosen+[remainder[0]],remainder[1:],expectedsum) + checksum(chosen,remainder[1:],expectedsum)
arr=[1,2,1]
expectedsum=2
print(f"Printing all sum {checksum([],arr,expectedsum)}")

#print first some equal to given sum

def printFirstsum(chosen,remainder,expectedsum):
    if len(remainder)==0:
        if sum(chosen)==expectedsum:
            return chosen
        return False
    return printFirstsum(chosen+[remainder[0]],remainder[1:],expectedsum) or printFirstsum(chosen,remainder[1:],expectedsum)

arr=[1,2,1]
expectedsum=3
# print("printsum",printFirstsum([],arr,expectedsum))

#print count of all the element combination euqal to sum

def printSumCount(chosen,remainder,expectedsum):
    # if sum(chosen)>expectedsum:
    #     return 0
    if len(remainder)==0:
        if sum(chosen)==expectedsum:
            return 1
        return 0
    left=printSumCount(chosen+[remainder[0]],remainder[1:],expectedsum)
    right=printSumCount(chosen,remainder[1:],expectedsum)
    return left+right

arr=[1,2,1]
expectedsum=2

print("print sum count",printSumCount([],arr,expectedsum))


#print combination sum
ans=[]
def combinationSum(arr,index,target,ds):
    if target==0 :
        ans.append(ds)
        return
    if len(arr) == index or target<0:
        return
    combinationSum(arr,index,target-arr[index],ds+[arr[index]])
    combinationSum(arr,index+1,target,ds)


combinationSum([2,3,6,7],0,7,[])
print(f"combinationSum {ans}")


map={"count":0}
def combinationSum4(arr,index,target,dp):
    if target==0 :
        return 1
    if len(arr) == index or target<0:
        return 0
    if dp[target]!=-1:
        return  dp[target]
    for i in range(0,len(arr)):
        map["count"]+=combinationSum4(arr,i,target-arr[i],dp)

    dp[target]=map['count']
    return  dp[target]

dp=[-1]*(len(arr)+1)


# print(f"combinationSum 4 {combinationSum4([1,2,3],0,4,dp)}")

ans=[]
def combinationSum2(arr,index,target,ds):
    if target==0 :
        ans.append(ds)
        return
    if len(arr) == index or target<0:
        return
    prevIndex=-1
    for i in range(index,len(arr)):
        if prevIndex==arr[i]:
            continue
        else:
            prevIndex=arr[i]
        if arr[i]>target:
            break

        combinationSum2(arr,i+1,target-arr[i],ds+[arr[i]])
ar=[1,1,1,2,2]
ar.sort()
combinationSum2(ar,0,4,[])
print("combination sum2  ",ans)

ans=[]
def combinationSum2brute(arr,index,target,ds):
    if target==0 :
        if ds not in ans:
            ans.append(ds)
        return
    if len(arr) == index or target<0:
        return
    combinationSum2brute(arr,index+1,target-arr[index],ds+[arr[index]])
    combinationSum2brute(arr, index + 1, target, ds)
ar=[1,1,1,2,2]
ar.sort()
# print(ar)
combinationSum2brute(ar,0,4,[])
print("combination sum2 bruce ",ans)

ans=[]

def subsetSum(arr,index,res):
    if index==len(arr):
        ans.append(res)
        return
    subsetSum(arr,index+1,res+arr[index])
    subsetSum(arr,index+1,res)


arr=[3,1,2]
subsetSum(arr,0,0)
print("subset sum",ans)


#Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
ans=[]
def subset2brute(arr,index,ds):
    if len(arr)==index:
        if ds not in ans:
            ans.append(ds)
        return
    subset2brute(arr,index+1,ds+[arr[index]])
    subset2brute(arr,index+1,ds)

ar=[1,2,2]
subset2brute(ar,0,[])
print("subset sum2 ",ans)


ans=[]
def subset2opt(arr,index,ds):
    ans.append(ds)
    prev=-1
    for i in range(index,len(arr)):
        if arr[i]==prev:
            continue
        else:
            prev=arr[i]
        subset2opt(arr,i+1,ds+[arr[i]])

ar=[1,2,2]
subset2opt(ar,0,[])
print("subset sum2 opt ",ans)

##print all permutation of  string (using extra map )

ans=[]
def printPermutation(arr,ds,map):
    if len(ds)==len(arr):
        ans.append(ds[:])
        return
    for i in range(0,len(arr)):
        if map[i]==0:
            map[i]=1
            ds.append(arr[i])
            printPermutation(arr,ds,map)
            ds.pop()
            map[i]=0

map=[0]*len(arr)
#
printPermutation([1,2,3],[],map)
print(ans)

#print permutation of string  (without using extra map )
res=[]
def permute(arr,index):
    if index==len(arr):
        res.append(arr[:])
        return
    for i in range(index,len(arr)):
        arr[i],arr[index]=arr[index],arr[i]
        permute(arr,index+1)
        arr[i], arr[index] = arr[index], arr[i]


permute([1,2,3],0)
print("permutation",res)











