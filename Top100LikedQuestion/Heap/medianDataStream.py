from heapq import  heappop,heappush
class MedianFinder(object):

    def __init__(self):
        self.small,self.large=[],[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.small,-num)

        if self.small and self.large and - self.small[0] > self.large[0]:
            val=-heappop(self.small)
            heappush(self.large,val)
        if len(self.small) > len(self.large) + 1:
            val = -heappop(self.small)
            heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush(self.small, -val)


    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.small)+len(self.large))%2==0:
            return (self.large[0]-self.small[0])/2.0
        else:
            if len(self.small)>len(self.large):
                return  -self.small[0]
            else:
                return self.large[0]

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
num=6
obj.addNum(num)
# param_2 = obj.findMedian()
# print(param_2)
num=10
obj.addNum(num)
# param_2 = obj.findMedian()
# print(param_2)
num=2
obj.addNum(num)
# param_2 = obj.findMedian()
# print(param_2)
num=6
obj.addNum(num)
# param_2 = obj.findMedian()
# print(param_2)
num=5
obj.addNum(num)
# param_2 = obj.findMedian()
# print(param_2)
num=0
obj.addNum(num)
# param_2 = obj.findMedian()
# print(param_2)
# num=6
# obj.addNum(num)
# param_2 = obj.findMedian()
# print(param_2)
# num=3
# obj.addNum(num)
# param_2 = obj.findMedian()
# print(param_2)
# num=1
# obj.addNum(num)
# param_2 = obj.findMedian()
# print(param_2)
# num=0
# obj.addNum(num)
# param_2 = obj.findMedian()
# print(param_2)
# num=0
# obj.addNum(num)
# param_2 = obj.findMedian()
# print(param_2)


