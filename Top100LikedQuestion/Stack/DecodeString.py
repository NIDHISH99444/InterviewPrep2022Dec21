def decodeString(arr):
    stack=[]
    for i in range(len(arr)):
        if arr[i]==']':
            res=''
            while stack[-1]!='[':
                res+=stack.pop()
            stack.pop()
            res=res[::-1]
            finalNo=''
            while len(stack) and stack[-1].isdigit():
                num=stack.pop()
                finalNo+=num
            finalNo=int(finalNo[::-1])
            res=finalNo*res
            for ele in res:
                stack.append(ele)
        else:
            stack.append(arr[i])
    return "".join(stack)


s = "10[leetcode]"

s="3[a]2[bc]"
print(decodeString(s))