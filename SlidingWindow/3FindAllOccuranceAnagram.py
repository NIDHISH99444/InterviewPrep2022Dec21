def  findAllAnagram(s,p):
    map,res={},[]
    i,j,=0,0

    for ele in p:
        if ele not in map:
            map[ele]=1
        else:
            map[ele]+=1
    cnt=len(map)
    while j<len(s):
        if s[j] in map:
            map[s[j]]-=1
            if map[s[j]]==0:
                cnt-=1
        if j-i+1 == len(p):
            if cnt==0:
                res.append(i)
            if s[i] in map:
                map[s[i]]+=1
                if map[s[i]]==1:
                    cnt+=1
            i+=1
        j+=1
    return res




s = "cbaebabacd"
p = "aabc"

print(findAllAnagram(s,p))