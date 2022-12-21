def buysellMaxProfit(arr):
    maxProfit=float('-inf')
    minVal=float('inf')
    for i in range(len(arr)):
        minVal=min(minVal,arr[i])
        maxProfit=max(maxProfit,arr[i]-minVal)
    return maxProfit



prices = [7,1,5,3,6,4]
print(buysellMaxProfit(prices))


