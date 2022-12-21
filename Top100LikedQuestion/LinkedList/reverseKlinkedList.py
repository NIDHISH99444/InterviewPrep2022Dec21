
class ListNode:
	def __init__(self, data):
		self.val = data
		self.next = None

def reverseKGroup( head, k):
    dummy =ListNode(0)
    dummy.next =head
    prev=dummy
    tst =head
    count =0
    while tst:
        count+=1
        tst =tst.next
    while count>=k:
        curr=prev.next
        nxt=curr.next
        for i in range(k-1):
            curr.next =nxt.next
            nxt.next =prev.next
            prev.next =nxt
            nxt =curr.next
        count-=k
        prev=curr
    return dummy.next

def printList(node):
    while (node != None):
        print(node.val,
              end=" ")
        node = node.next

k=2

arr = ListNode(1)
arr.next = ListNode(2)
arr.next.next = ListNode(3)
arr.next.next.next = ListNode(4)
arr.next.next.next.next = ListNode(5)
printList(arr)
print()
head=reverseKGroup(arr,k)
printList(head)