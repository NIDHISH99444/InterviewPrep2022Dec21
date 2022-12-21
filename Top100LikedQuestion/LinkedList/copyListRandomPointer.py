# """
# # Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random



def copyRandomList( head):
    """
    :type head: Node
    :rtype: Node
    """
    if not head: return None
    # create copied nodes and add in bw curr and next
    curr = head
    while curr:
        copyNode = Node(curr.val, curr.next)
        curr.next = copyNode
        copyNode.next =curr.next
        curr = curr.next.next

        # Iterate thru again and assign copied now
    curr = head
    while curr:

        if curr.random is not None:
            copiedRandom = curr.random.next
            curr.next.random = copiedRandom

        curr = curr.next.next

        # Create new DeepList copy
    curr=head
    deepCopyHead = head.next
    while curr:
        temp=curr.next.next
        copy=curr.next
        curr.next=temp
        if temp:
            copy.next=temp.next
        curr=temp

    return deepCopyHead



def printList(node):
    while (node != None):
        print(node.val,
              end=" ")
        node = node.next


arr = Node(7,13,None)
arr.next = Node(13,11,0)
arr.next.next = Node(11,10,4)
arr.next.next.next = Node(10,1,2)
arr.next.next.next.next = Node(1,None,0)


head=copyRandomList(arr)
printList(head)