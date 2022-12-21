from collections import  defaultdict
from heapq import heappush,heappop
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def rightSideView(root):
    if not root :
        return
    queue=[root]
    ll=[]

    while queue:
        flag=0
        for i in range(len(queue)):
            node=queue.pop(0)
            if flag==0:
                flag=1
                res.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
    return res

def leftLeaf(root):
    if not root:
        return
    queue = [root]
    ll = []
    sum=0
    while queue:

        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                ele=node.left
                if not ele.left and not ele.right:
                    sum+=ele.val
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return sum

res=[]
def treePath(root,path):
    if not root:
        return
    path += str(root.val) + "->"
    if not root.left and not root.right:
        res.append(path[:-2])
        return

    treePath(root.left, path)
    treePath(root.right, path)

maxCount=0
def maxDepth(root,cnt):
    if not root :
        return cnt
    cnt+=1
    leftC=maxDepth(root.left,cnt)
    rightC=maxDepth(root.right,cnt)
    return max(leftC,rightC)

def isSymmetric(root):
    if not root:
        return True
    root1=root.left
    root2=root.right
    def checkSym(root1,root2):
        if (not root1 and root2 )  or (not root2 and root1):
            return False
        if not root1 and not root2:
            return True
        return root1.val==root2.val and checkSym(root1.left,root2.right) and checkSym(root1.right,root2.left)
    return (checkSym(root1,root2))


def diameter(root):
    global maxi
    if not root:
        return 0
    left=diameter(root.left)
    right=diameter(root.right)
    maxi=max(maxi,left+right)
    return 1+max(left,right)



def isBalanced2(root):

    if not root:
        return 0
    leftC = isBalanced2(root.left)
    rightC = isBalanced2(root.right)
    if leftC == -1 or rightC == -1:
        return -1
    if abs(leftC - rightC) <= 1:
        return 1 + max(leftC, rightC)
    else:
        return -1




def zigZagTraversal(root):
    if not root:
        return []
    s1,s2=[],[]
    s1.append(root)
    ll=[]

    while s1 or s2 :
        res=[]
        while s1:
            ele=s1.pop()
            res.append(ele.val)
            if ele.left:
                s2.append(ele.left)
            if ele.right:
                s2.append(ele.right)

        ll.append(res)
        res=[]
        while s2 :
            ele=s2.pop()
            res.append(ele.val)
            if ele.right:
                s1.append(ele.right)
            if ele.left:
                s1.append(ele.left)

        ll.append(res)
    print("ll",ll)
    if not ll[-1]:
        return ll[:-1]
    return ll


def lowestCommonAncestor( root, p, q):
    if not root:
        return
    if root.val==p or root.val==q :
        return root.val
    left=lowestCommonAncestor(root.left,p,q)
    right=lowestCommonAncestor(root.right,p,q)
    if left and right:
        return root.val
    return left or right


def validateBinarySearchTree(root, l=float('-inf'), r=float('inf')):
    if not root :
        return True
    if root.val <= l or root.val >=r:
        return False

    return validateBinarySearchTree(root.left,l,root.val) and validateBinarySearchTree(root.right,root.val,r)
val=[]


# def kthSmallest(root):
#     global k
#     if not root :
#         return
#     left=kthSmallest(root.left)
#     k-=1
#     if k==0:
#         return root.val
#     right=kthSmallest(root.right)
#     if left or right:
#         return left or right


import sys
global ceil
ceil=sys.maxsize
res.append(ceil)
def findCeil(root, x,ceil):
    # Write your code here.

        if not root :
            return False
        if root.val ==x:
            return root.val
        if root.val > x:
            ceil=min(res.pop(0),root.val)
            res.append(ceil)
            findCeil(root.left,x,ceil)
        else:
            findCeil(root.right,x,ceil)

# def kthsmallest(root,cnt,k):
#     if not root:
#         return False
#     cnt+=1
#     left=kthsmallest(root.left,cnt,k)
#     if left:
#         return left
#     if cnt==k:
#         return root.val
#     return kthsmallest(root.right, cnt, k)

left_end=-sys.maxsize
right_end=sys.maxsize
def isValidBST( root,left_end,right_end):
    if not root:
        return True
    if root.val < left_end or root.val > right_end:
        return False
    return  isValidBST(root.left,left_end,root.val) and isValidBST(root.right,root.val,right_end)

def lowestCommonAncestor( root, p, q):
    if root==p or root==q or not root:
        return root
    if root.val>=p and root.val<=q:
        return  root.val
    left=lowestCommonAncestor(root.left,p,q)
    right=lowestCommonAncestor(root.right,p,q)
    if left and right:
        return  root
    else:
        return left or right



def verticalTraversal(root,mp,h):
    if not root:
        return
    mp[h].append(root.val)
    verticalTraversal(root.left, mp, h-1)
    verticalTraversal(root.right, mp, h + 1)




def maxPathSum(root):
    if not root:
        return 0
    left = max(maxPathSum(root.left), 0)
    right = max(maxPathSum(root.right), 0)
    res.append(max(res.pop(0), root.val + left + right))
    return root.val + max(left, right)


def createTree(inorder,preorder):
    if inorder:
        index=inorder.index(preorder.pop(0))
        root=Node(inorder[index])
        root.left=createTree(inorder[0:index],preorder)
        root.right=createTree(inorder[index+1:],preorder)
        return root

def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.val)
    printInorder(root.right)

preorder=[20,40,50]
inorder=[40,20,50]
root=createTree(inorder,preorder)
# printInorder(root)


def serialize(root):
    q=[root]
    ans=[]
    while q:
        node=q.pop(0)
        if node:
            q.append(node.left)
            q.append(node.right)
            ans.append(str(node.val))
        else:
            ans.append("#")
    return ','.join(ans)

def deserialize( data):
    def createNode(strVal):
        if strVal == "#": return None
        return Node(int(strVal))

    if data == "#": return None
    strs = data.split(",")
    root = createNode(strs[0])
    i = 1
    bfs = [root]
    while bfs:
        curr = bfs.pop(0)
        curr.left = createNode(strs[i])
        curr.right = createNode(strs[i+1])
        i += 2
        if curr.left != None:
            bfs.append(curr.left)
        if curr.right != None:
            bfs.append(curr.right)

    return root


#
# def widthTree(root):
#     cnt=0
#     q=[(root,cnt)]
#     maxr=-sys.maxsize
#     while q :
#
#         first=q[0][0]
#         curr=None
#         for i in range(len(q)):
#             node,cnt=q.pop(0)
#             if node.left:
#                 q.append((node.left,2*cnt))
#             if node.right:
#                 q.append((node.right,2*cnt+1))
#         maxr=max(maxr,q[-1][0].val-firstIndex+1)
#     return maxr
#




# root = Node(2)
# root.left = Node(1)
# root.right = Node(3)
# root.left.left = Node(6)
# root.left.right = Node(2)
# root.right.left= Node(0)
# root.right.right= Node(8)
# root.left.right.left=Node(7)
# root.left.right.right=Node(4)
# root.right.right = Node(3)
# res = isBalanced(root, 0)

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(6)
root.left.left.left = Node(4)
root.left.left.right = Node(7)
# root.right.left= Node(0)
# root.right.right= Node(7)
# root.left.left.left=Node(1)

val = isBalanced2(root)

if val != -1:
    print(True)
else:
    print(False)
# findCeil(root,7,ceil)
# print(res)
#print(kthSmallest(root))
# print(val[k-1])
# root.left.right.right=Node(4)
# root.right.right = Node(3)
# print(validateBinarySearchTree(root))
# isBalanced(root,0)
path=""
print(treePath(root,path))
print(res)
# print(zigZagTraversal(root))
#print(rightSideView(root))
# print(lowestCommonAncestor( root, 3, 6))
# print(maxDepth(root,0))
# print(isSymmetric(root))
# print(levelOrderTraversal(root))
# print("sum ",leftLeaf(root))
# cnt=0
# k=3
# print(kthsmallest(root,cnt,k))

# print(isValidBST( root,left_end,right_end))
# p,q=3,6
# print(lowestCommonAncestor( root, p, q))
# mp=defaultdict(list)
# verticalTraversal(root,mp,0)
#
# res=[]
# for key in sorted(mp.keys()):
#     res.append(sorted(val))
# print(res)
# res=[-sys.maxsize]
# maxi=-sys.maxsize
# maxPathSum(root)
# print(res[0])
# data=serialize(root)
# root=deserialize(data)
# printInorder(root)
# # widthTree(root)
maxi=float('-inf')
diameter(root)
print("maxDia",maxi)

