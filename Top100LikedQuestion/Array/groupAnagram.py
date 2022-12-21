



def ana(strs):
    dict={}
    for str in strs:
        key="".join(sorted(str))
        if key not in dict:
            dict[key]=[str]
        else:
            dict[key].append(str)
    res=[]
    for _,val in dict.items():
        res.append(val)
    return (res)
strs = ["eat" ,"tea" ,"tan" ,"ate" ,"nat" ,"bat"]
print(ana(strs))