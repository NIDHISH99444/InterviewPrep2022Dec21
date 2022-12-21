class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self,cap):
        self.capacity=cap
        self.dict={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head


    def set(self,key,val):
        if key in self.dict:
            node=self.dict[key]
            self._remove(node)
        newNode=Node(key, val)
        self.dict[key]=newNode
        self._add(newNode)
        if len(self.dict)>self.capacity:
            removedNode=self.head.next
            self._remove(removedNode)
            del self.dict[removedNode.key]


    def get(self,key):
        if key not in self.dict:
            return -1
        node=self.dict[key]
        self._remove(node)
        self._add(node)
        return node.val


    def _remove(self,node):
        prevNode=node.prev
        nextNode=node.next
        prevNode.next=nextNode
        nextNode.prev=prevNode


    def _add(self,node):
        secLastNode=self.tail.prev
        secLastNode.next=node
        node.prev=secLastNode
        node.next=self.tail
        self.tail.prev=node



obj=LRUCache(3)

obj.set("imperva", "red")
obj.set("imperva1", "blue")
obj.set("imperva3", "orange")

print(obj.get("imperva1"))

obj.set("imperva4", "yellow")
print("imperva : ", obj.get("imperva"))
