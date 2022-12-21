

def gasStation(gas,cost):
    if sum(gas)<sum(cost):
        return -1
    ans=0
    remaining_fuel=0
    for i in range(len(gas)):
        remaining_fuel+=gas[i]-cost[i]
        if remaining_fuel < 0:
            ans=i+1
            remaining_fuel=0
    return ans



gas=[5,1,2,3,4]
cost=[4,4,1,5,1]

print(gasStation(gas,cost))