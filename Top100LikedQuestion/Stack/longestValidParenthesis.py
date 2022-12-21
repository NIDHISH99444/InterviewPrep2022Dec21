def longestValidParenthesis(arr):
    stack,indexStack=[],[-1]
    maxLen=0
    for i in range(len(arr)):
        if arr[i]=='(':
            stack.append(arr[i])
            indexStack.append(i)
        elif arr[i]==')':
            if not stack or stack[-1]!='(':
                indexStack.append(i)
            else:
                stack.pop()
                indexStack.pop()
                maxLen=max(maxLen,i-indexStack[-1])
    return maxLen



s = ")()())"
print(longestValidParenthesis(s))

