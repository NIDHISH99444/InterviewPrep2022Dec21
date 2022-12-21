def valid(arr):
    stack=[]
    dict = {"]": "[", "}": "{", ")": "("}

    for ele in arr:
        if ele in dict.values():
            stack.append(ele)
        elif ele in dict.keys():
            if not len(stack) or  dict[ele]!=stack.pop():
                return False
    return len(stack)==0


s = "([]{})"
print(valid(s))