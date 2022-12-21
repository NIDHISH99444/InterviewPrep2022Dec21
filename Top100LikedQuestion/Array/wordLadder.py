

def wordLadder(wordList,beginWord,endWord):
    myset=set()
    for ele in wordList:
        myset.add(ele)
    cnt=0
    q=[]
    q.append((beginWord,1))
    while q :
        word,cnt=q.pop(0)
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                newword=word[:i]+char+word[i+1:]
                if newword==endWord:
                    return  cnt+1
                if newword in myset:
                    myset.remove(newword)
                    q.append((newword,cnt+1))
                    print(q)

    return 0






beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

# print(ladderLength(beginWord,endWord,wordList))

print("word is ",wordLadder(wordList,beginWord,endWord))