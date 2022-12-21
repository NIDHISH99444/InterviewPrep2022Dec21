
res=[]
def letterCombination(digit,output,index,mapping):
    if index==len(digit):
        res.append(output)
        return
    element=digit[index]
    string=mapping[int(element)]
    for stri in string:
        output1=output
        output+=stri
        letterCombination(digit,output,index+1,mapping)
        output=output1



digit="13"
output=""
mapping=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
letterCombination(digit,output,0,mapping)
print(res)
