# Pointers to remember
# 1> Adding  list  and string
#     lst =[]
#     str="a"
#     res=lst+[str]
#     Convert string into list and append to list
# 2> Adding 2 string
#     str1=""
#     str2=""
#     str3=str1+str2
# 3> Making shalow copy of  variable using arr[:] when we are updating into final result , otherwise array gets
#     updated in final call


lst=[1,3,4]
lst.sort()
print(lst)

str="afdsb"
key="".join(sorted(str))
print(key)

interval=[[1,2],[2,5],[1,6],[3,3]]

# Sorting with first element
# 1> interval.sort()
interval.sort(key=lambda x : x[0])

str="A"
print(str.lower())
str=" "
print(str.isalnum())
# Sorting with last element
print(interval)
interval.sort(key=lambda x : x[1])
print(interval)
