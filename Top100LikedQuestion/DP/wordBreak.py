from typing import  List
def wordBreak( s: str, wordDict: List[str]) -> bool:
    n=len(s)
    wordDic=set(wordDict)
    def dp(start):
        if start==n:
            return True
        for end in range(start,n):
            word=s[start:end+1]
            if word in wordDic and dp(end+1):
                return True
        return False

    return dp(0)


s = "catsandog"
wordDict = ["cats","og","sand","and","cat"]

print(wordBreak(s,wordDict))