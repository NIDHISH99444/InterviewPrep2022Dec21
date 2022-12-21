
def pascalTri(num):
    final_list=[]
    for i in range(num):
        ll=[1]*(i+1)
        final_list.append(ll)

    for i in range(2,len(final_list)):
        for j in range(1,len(final_list[i])-1):
            final_list[i][j]=final_list[i-1][j-1]+final_list[i-1][j]
    return final_list




n=5
print(pascalTri(n))