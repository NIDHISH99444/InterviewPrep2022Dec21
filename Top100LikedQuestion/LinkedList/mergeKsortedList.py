from  heapq import  heappush,heappop
class ListNode:
	def __init__(self, data):
		self.val = data
		self.next = None

def mergeKLists( lists):
    dummy=curr=ListNode(0)
    heap=[]
    for ind,ele in enumerate(lists):
        if ele:
            heappush(heap,(ele.val,ind))

    while heap:
        ele,ind=heappop(heap)
        curr.next=ListNode(ele)
        curr=curr.next
        if lists[ind].next:
            lists[ind]=lists[ind].next
            heappush(heap,(lists[ind].val,ind))
    return dummy.next


def printList(node):
    while (node != None):
        print(node.val,
              end=" ")
        node = node.next

# lists = [[1,4,5],[1,3,4],[2,6]]


arr = [None for i in range(3)]
print(arr)
arr[0] = ListNode(1)
arr[0].next = ListNode(4)
arr[0].next.next = ListNode(5)


arr[1] = ListNode(1)
arr[1].next = ListNode(3)
arr[1].next.next = ListNode(4)


arr[2] = ListNode(2)
arr[2].next = ListNode(6)
print(arr)
head=mergeKLists(arr)
printList(head)
