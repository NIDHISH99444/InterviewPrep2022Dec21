def generateParenthesis( n):

    ans = []

    def generate(res, open, close):
        if open == 0 and close == 0:
            ans.append(res)
            return
        if open > 0:
            generate(res + "(", open - 1, close)
        if close > open:
            generate(res + ")", open, close - 1)

    open, close = n, n
    generate("", open, close)
    return ans


arr=[7, 1, 5, 3, 6, 4]

print(generateParenthesis(3))