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

    def print(self):
        start=self.head
        while start!=None:
            print(start.data)
            start=start.next

    def getIntersectionNode(self,ll1,ll2):
        len1,len2=0,0
        head1=ll1
        head2=ll2
        while ll1 != None:
            len1+=1
            ll1=ll1.next
        while ll2 != None:
            len2 += 1
            ll2 = ll2.next
        if len1>len2:
            diff=len1-len2
            slow=head1
            while diff>0:
                slow=slow.next
                diff-=1
            while slow!=None:
               if slow.data==head2.data:
                   return True
            return False
        else:
            diff=len2-len1
            slow = head2
            while diff > 0:
                slow = slow.next
                diff -= 1
            while slow != None:
                if slow.data == head1.data:
                    return True
            return False





# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

llist1 = LinkedList()
llist1.push(20)
llist1.push(4)
llist1.push(2)
llist1.push(1)

# Create a loop for testing


# print(llist.getIntersectionNode(llist,llist1))
print(llist.print())

