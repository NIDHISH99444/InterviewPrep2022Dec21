words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"


def compare(word1,word2,dict):
    i,j=0,0
    while i < len(word1) and j<len(word2) :
        if dict[word1[i]]==dict[word2[j]]:
            i+=1
            j+=1
        elif dict[word1[i]]<dict[word2[j]]:
            return True
        else:
            return False
    if i==len(word1) and j!=len(word2):
        return False


def result(words,order):
    dict={}
    for i,j in enumerate(order):
        dict[j]=i
    for i in range(len(words)-1):
        if not compare(words[i],words[i+1],dict):
            return  False
    return True



print("Final res",result(words,order))