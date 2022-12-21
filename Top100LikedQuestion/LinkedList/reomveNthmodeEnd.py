
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LL:
    def __init__(self):
        self.head=None

    def push(self, val):
        if self.head is None:
            self.head = ListNode(val)
        else:
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = ListNode(val)

    def print(self,head):
        start = head
        while start != None:
            print(start.val)
            start = start.next

    def reverseList(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head=self.head
        dummy = None
        start = head
        while start != None:
            nxt = start.next
            start.next = dummy
            dummy = start
            start = nxt
        return dummy

l=LL()
l.push(1)
l.push(2)
l.push(3)
# l.print()
head=l.reverseList()
l.print(head)

