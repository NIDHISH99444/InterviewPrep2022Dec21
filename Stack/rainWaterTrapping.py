def rainWaterTrapping(arr):
    maxLeft=[0]*len(arr)
    maxRight=[0]*len(arr)
    maxLeft[0]=arr[0]
    maxRight[len(arr)-1]=arr[len(arr)-1]
    for i in range(1,len(arr)):
        maxLeft[i]=max(maxLeft[i-1],arr[i])
    for j in range(len(arr)-2,-1,-1):
        maxRight[j]=max(maxRight[j+1],arr[j])
    print(maxLeft)
    print(maxRight)
    totalWater=0
    for i in range(len(arr)):
        totalWater+=(min(maxLeft[i],maxRight[i])-arr[i])

    print(totalWater)


rainWaterTrapping([0,1,0,2,1,0,1,3,2,1,2,1])