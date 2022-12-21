res=[]
def printAllSusequences(arr,index,ds):
    if index==len(arr):
        res.append("".join(ds))
        return
    printAllSusequences(arr,index+1,ds+[arr[index]])
    printAllSusequences(arr,index+1,ds)
#
# printAllSusequences("123",0,[])
# print(res)

res=[]
def subSetEaualToSum(arr,finalsum,index,ds):
    if len(arr)==index:
        if finalsum==sum(ds):
            return 1
        return 0
    left=subSetEaualToSum(arr,finalsum,index+1,ds+[arr[index]])
    right=subSetEaualToSum(arr,finalsum,index+1,ds)
    return left+right

print(subSetEaualToSum([1,2,1],2,0,[]))

