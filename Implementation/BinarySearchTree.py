class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
# ---------- insert a new node with the given key in BST ----------
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
 
    # Return the (unchanged) node pointer
    return node

# ---------- search a key in a BST ----------
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.key == key:
        return root
 
    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)
 
    # Key is smaller than root's key
    return search(root.left, key)

# ---------- deletes the key and returns the new root ----------
def deleteNode(root, key):
    # base Case
    if root is None:
        return root
 
    # If the key to be deleted is
    # smaller than the root's key,
    # then it lies in left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
 
    # If the key to be deleted is
    # greater than the root's key,
    # then it lies in right subtree
    elif key > root.key:
 
        root.right = deleteNode(root.right, key)
 
    # If key is same as root's key,
    # then this is the node
    # to be deleted
    else:
 
        # Node with only one child
        # or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        # Node with two children:
        # Get the inorder successor(smallest
        # in the right subtree)
        temp = minValueNode(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.key = temp.key
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
 
    return root

# ---------- traversal/print functions ----------
# ---------- inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# ---------- preorder traversal
def preOrder(root):
    if root:
        print(root.key, end=" ")
        preOrder(root.left)
        preOrder(root.right)

# ---------- postorder traversal
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.key, end=" ")

# ---------- print nodes at a given level
 def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.key, end=' ')
    elif level > 1:
        # Recursive Call
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)

# ---------- print leaf nodes from left to right
def printLeafNodes(root):
    # If node is null, return
    if not root:
        return
 
    # If node is leaf node,
    # print its data
    if not root.left and not root.right:
        print(root.key, end=" ")
 
    # If left child exists,
    # check for leaf recursively
    if root.left:
        printLeafNodes(root.left)
 
    # If right child exists,
    # check for leaf recursively
    if root.right:
        printLeafNodes(root.right)

# ---------- print height of the BST
def height(node):
    if node is None:
        return 0
    else:
        # Compute the depth of each subtree
        lDepth = height(node.left)
        rDepth = height(node.right)
 
        # Use the larger one
        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1