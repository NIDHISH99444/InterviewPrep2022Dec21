import sys


class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None



res=[]
def printPath(root,path):
    if not root:
        return
    path += str(root.val)
    if not root.left and not root.right:
        res.append(path)
        return

    printPath(root.left,path)
    printPath(root.right,path)

maxi=-sys.maxsize
def printMaxPathrootToleaf(root,path):
    global maxi
    if not root:
        return
    path += root.val
    if not root.left and not root.right:
        maxi=max(maxi,path)
        return

    printMaxPathrootToleaf(root.left,path)
    printMaxPathrootToleaf(root.right,path)



def verticalTrav(root,m,hd):
    if not root:
        return
    m[hd].append(root.val)
    verticalTrav(root.left, m, hd-1)
    verticalTrav(root.right, m, hd+1)



def leftView(root):
    mp={}
    hd=0

    q=[root]
    while q:
        flag=0
        for i in range(len(q)):
            node = q.pop(0)
            if flag==0:
                res.append(node.val)
            flag=1


            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
    print(res)

def printRootToLeaf(root,nodeVal,path):
    if not root:
        return False
    path+=str(root.val)
    if root.val==nodeVal:
        return path
    left=printRootToLeaf(root.left,nodeVal,path)
    right=printRootToLeaf(root.right,nodeVal,path)
    return left or right
import sys
res=[-sys.maxsize]

def diameter(root):

    if not root :
        return 0
    lh=diameter(root.left)
    rh=diameter(root.right)

    res.append(max(res.pop(0),lh+rh))
    return 1+max(lh,rh)


def leftTraversal(root):
    if root :

        if root.left:
            print(root.val)
            leftTraversal(root.left)
        elif root.right:
            print(root.val)
            leftTraversal(root.right)

def printLeaf(root):
    if not root:
        return
    if not root.left and not root.right:
        print(root.val)
        return
    printLeaf(root.left)
    printLeaf(root.right)

def cousin(root,x,y):
    res=[]
    def dfs(root,parent,depth):
        if not root:
            return
        if root.val==x or root.val==y:
            res.append((parent.val,depth))
        dfs(root.left,root,depth+1)
        dfs(root.right,root,depth+1)

    dfs(root,None,0)

    val_x,val_y=res
    return val_x[0]!=val_y[0] and val_x[1]==val_y[1]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.left.left = Node(7)
root.right.left.left.left = Node(8)
# printPath(root,"")
# print(res)
from collections import defaultdict
m=defaultdict(list)
verticalTrav(root,m,0)
print(m)
for key,values in  m.items():
    print(values)
#for top view
for key,values in  m.items():
    print(values[0])

# leftView(root)

# path=''
# print(printRootToLeaf(root,6,path))

# diameter(root)
# print(res[0])

# leftTraversal(root)
# printLeaf(root)
# print(cousin(root,5,6))
# printMaxPathrootToleaf(root,0)
# print(maxi)