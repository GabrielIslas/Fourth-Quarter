class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        self.parent = None
    
def insert(root, key):
    y = None
    x = root
    z = Node(key)

    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
            
    z.parent = y

    if root is None:
        return z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

    return root
# O(n)
def preorder_tree_walk(r):
    if r is not None:
        print(r.key, end = " ")
        preorder_tree_walk(r.left)
        preorder_tree_walk(r.right)
# O(n)
def postorder_tree_walk(r):
    if r is not None:
        postorder_tree_walk(r.left)
        postorder_tree_walk(r.right)
        print(r.key, end = " ")
# O(n)
def inorder_tree_walk(r):
    if r is not None:
        inorder_tree_walk(r.left)
        print(r.key, end = " ")
        inorder_tree_walk(r.right)
# O(h)
def tree_search(x, k):
    if x is None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)
# O(h)    
def iterative_tree_search(x, k):
    while x is not None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x
# O(h)
def minimum(x):
    currentNode = x
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode.key
# O(h)
def maximum(x):
    currentNode = x
    while currentNode.right is not None:
        currentNode = currentNode.right
    return currentNode.key

def successor(x):
    if x.right != None:
        return minimum(x.right)
    y = x.parent
    while y.left != x and y is not None:
        x = y
        y = x.parent
    return y.key

def predecessor(x):
    if x.left != None:
        return maximum(x.left)
    y = x.parent
    while y.right != x and y is not None:
        x = y
        y = x.parent
    return y.key

    

r = insert(None, 18)
r = insert(r, 7)
r = insert(r, 34)
r = insert(r, 21)
r = insert(r, 19)
r = insert(r, 32)
r = insert(r, 5)

postorder_tree_walk(r)

