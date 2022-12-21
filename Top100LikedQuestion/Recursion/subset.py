

ans=[]
def subset(num,res):
    if not len(num):
        ans.append(res)
        return

    subset(num[1:],res+[num[0]])
    subset(num[1:],res)




num=[1,2,3]
subset(num,[])
print(ans)