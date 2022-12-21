# Python3 program to detect loop
# in the linked list

# Node class
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,newdata):
        newdata=Node(newdata)
        newdata.next=self.head
        self.head=newdata

    def detectLoop(self):
        slow,fast=self.head,self.head
        while fast!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

print(llist.detectLoop())
