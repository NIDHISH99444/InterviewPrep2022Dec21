
ans=[]
def generate(res,open,close):
    if open==0 and close==0 :
        ans.append(res)
        return
    if open>0:
        generate(res+"(",open-1,close)
    if close>open :
        generate(res + ")", open, close-1)





n=3
open,close=n,n
generate("",open,close)
print(ans)