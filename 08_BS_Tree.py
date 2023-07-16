from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Insert a new node and return the root of tD:\1 study\project\DSA\exp2.pyhe BST.
def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

# Return the minimum value node of the BST.
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def minValue(root):
    if root.left == None:
        return root.val
    else:
        return minValue(root.left)
def mixValue(root):
    if not root.right:
        return root.val
    else:
        return mixValue(root.right)

# Remove a node and return the root of the BST.
def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            remove(root.right, minNode.val)
    return root
#pre-order
'''def print_tree(root):
    ele=[]
    if root.left :
        ele += print_tree(root.left)
    
    if root.right:
        ele += print_tree(root.right)
    ele.append(root.val)

    return ele'''

def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
    

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)


def search(root,val):
    if not root:
        return print(False)
    if val > root.val:
         return search(root.right,val)
    elif val < root.val:
         return search(root.left,val)
    else:
        return print(True)

def bfs(root):
    queue = deque()
    if root:
        queue.append(root)
    level=0
    while len(queue)>0:
        print('level--',level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1

root = TreeNode(4)

insert(root,5)
insert(root,7)
insert(root,6)
insert(root,1)
insert(root,2)
insert(root,3)
insert(root,9)
insert(root,8)
#search(root,7)
#remove(root,7)
#search(root,7)
#print('pre_order-->')
#preorder(root)
#print('in_order-->')
#inorder(root)
#print('post_order-->')
#postorder(root)
bfs(root)