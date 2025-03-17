from OOPS.BinaryTree.BinaryTree import BinaryTree # ✅ Import the class, not the module
from OOPS.BinaryTree.TreeNode import TreeNode

def levelOrder(root):
    # Your code here
    queue = [root]
    output = [[root.data]]
    while(len(queue)!= 0):
        level = []
        node = queue.pop(0)
        if(node.left!=None):
            queue.append(node.left)
            level.append(node.left.data)
        if(node.right!=None):
            queue.append(node.right)
            level.append(node.right.data)
        if(len(level)!=0):
            output.append(level)
    return output

def hieghtOfATree(root):
    if(root == None):
        return -1
    leftHeight = hieghtOfATree(root.left) 
    rightHeight = hieghtOfATree(root.right)
    return max(leftHeight, rightHeight) +1

def isIdentical(r1, r2):
    if(r1 == None and r2 == None):
        return True
    if(r1.data == r2.data):
        return isIdentical(r1.left, r2.left) and isIdentical(r1.right, r2.right)
    else:
        return False
    
def isBalanced(root):
    if(root == None):
        return -1
    leftHeight = hieghtOfATree(root.left) 
    rightHeight = hieghtOfATree(root.right)
    return abs(leftHeight-rightHeight) <= 1

def checkBalanceOptimized(self, root):
    if root is None:
        return 0  # Height of an empty tree is 0
    
    # Get height of left subtree
    leftHeight = self.checkBalance(root.left)
    if leftHeight == -1:
        return -1  # If left subtree is unbalanced, stop checking
    
    # Get height of right subtree
    rightHeight = self.checkBalance(root.right)
    if rightHeight == -1:
        return -1  # If right subtree is unbalanced, stop checking
    
    # Check balance condition at current node
    if abs(leftHeight - rightHeight) > 1:
        return -1  # If imbalance is found, return -1
    
    # Return the height of the current subtree
    return max(leftHeight, rightHeight) + 1  

def isBalanced(self, root):
    return self.checkBalance(root) != -1

def isSumProperty(root):
    if root is None:
        return True  

    if root.left is None and root.right is None:
        return True 

    leftValue = root.left.data if root.left else 0
    rightValue = root.right.data if root.right else 0

    if root.data == leftValue + rightValue:
        return isSumProperty(root.left) and isSumProperty(root.right)
    else:
        return False


def widthOrder(root):
    queue = [root]
    output = 0
    while(len(queue)!= 0):
        
        level = []
        node = queue.pop(0)
        if(node.left!=None):
            queue.append(node.left)
            level.append(node.left.data)
        if(node.right!=None):
            queue.append(node.right)
            level.append(node.right.data)
        print(level)
    return output

def preOrder(root):
    #code here
    stack = [root]
    output = []
    while(len(stack)!=0):
        node = stack.pop(0)
        if(node.left is not None):
            stack.append(node.left)
        if(node.right is not None):
            stack.append(node.right)

        output.append(node.data)    
    return output

def findfloor(root, inp):
    
    ceilingValue = -1
    # code here
    while(root):
        if(root.data == inp):
            return root.data
        
        if(root.data < inp):
            ceilingValue = root.data
            root = root.right
        else:
            root = root.left
        
    return ceilingValue

def findCeil(root, inp):
    
    ceilingValue = -1
    # code here
    while(root):
        if(root.data == inp):
            return root.data
        
        if(root.data > inp):
            ceilingValue = root.data
            root = root.left
        else:
            root = root.right
        
    return ceilingValue

def minValue( root):
    ##Your code here
    if(root.left != None):
        return minValue(root.left)
    
    if(root.right != None):
        if(root.data == root.right.data):
            return root.right.data
        else:
            return root.data
    else:
        return root.data

def find_min(node):
    while node.left:
        node = node.left
    return node

def validateBinaryTree(root):

    if root is None:
        return True
    return ValidateBinaryTreeCalculate(root, float('-inf'), float('inf'))

def ValidateBinaryTreeCalculate(root, leftLimit, rightLimit):
    if root is None:
        return True
    if leftLimit > root.data or rightLimit < root.data:
        return False
    left = ValidateBinaryTreeCalculate(root.left, leftLimit, root.data)
    right = ValidateBinaryTreeCalculate(root.right, root.data,rightLimit)
    return left and right

def levelOrderTraversal(root):
    if not root:
        return []
    
    queue = [root]
    level = []
    while len(queue) > 0:
        data = []
        levelSize = len(queue)
        for _ in range(0, levelSize):
            node = queue.pop(0)
            if (node.left is not None) : queue.append(node.left)
            if (node.right is not None) : queue.append(node.right)
            data.append(node.data)
        level.append(data)
    return level

def rightSideView(root):
    if not root:
        return []
    
    rightViewNodes = []
    queue = [root]
    while len(queue) > 0:
        data = []
        levelSize = len(queue)
        for _ in range(0, levelSize):
            node = queue.pop(0)
            if (node.left is not None) : queue.append(node.left)
            if (node.right is not None) : queue.append(node.right)
            data.append(node.data)
        rightViewNodes.append(data[-1])
    return rightViewNodes

def leftSideView(root):
    if not root:
        return []
    
    leftNodes = []
    queue = [root]
    while len(queue) > 0:
        data = []
        levelSize = len(queue)
        for _ in range(0, levelSize):
            node = queue.pop(0)
            if (node.left is not None) : queue.append(node.left)
            if (node.right is not None) : queue.append(node.right)
            data.append(node.data)
        leftNodes.append(data[0])
    return leftNodes

def zigzagLevelOrder(root):
    if not root:
        return []
    direction = 0
    queue = [root]
    level = []
    while len(queue) > 0:
        data = []
        levelSize = len(queue)
        direction += 1

        for _ in range(0, levelSize):
            node = queue.pop(0)
            if (node.left is not None) : queue.append(node.left)
            if (node.right is not None) : queue.append(node.right)
            data.append(node.data)
        
        if direction % 2 != 0:
            level.append(data)
        else:
            level.append(data[::-1])
    return level



def zigZagTraversalGFG(root):
    if not root:
        return []
    direction = 0
    queue = [root]
    level = []
    
    while(len(queue)>0):
        data = []
        levelSize = len(queue)
        direction += 1
        
        for _ in range(0, levelSize):
            node = queue.pop(0)
            if(node.left is not None) : queue.append(node.left)
            if(node.right is not None) : queue.append(node.right)
            data.append(node.data)
        if(direction % 2 != 0):
            level.extend(data)
        else:
            level.extend(data[::-1])
    return level

def levelOrderTraversal(root):
    if not root:
        return []
    
    queue = [root]
    level = []
    while len(queue) > 0:
        data = []
        levelSize = len(queue)
        for _ in range(0, levelSize):
            node = queue.pop(0)
            if (node.left is not None) : queue.append(node.left)
            if (node.right is not None) : queue.append(node.right)
            data.append(node.data)
        level.append(data)
    return level[::-1]


# def diameterOfBinaryTree(root):
#     if not root:
#         return []
    
#     diameter = 0
#     queue = [root]
#     level = []
#     while len(queue) > 0:
#         data = []
#         levelSize = len(queue)
#         for _ in range(0, levelSize):
#             node = queue.pop(0)
#             if (node.left is not None) : queue.append(node.left) else: queue
#             if (node.right is not None) : queue.append(node.right)
#             data.append(node.data)

#         if(len(level) == 0):
#             diameter+=1
#             continue
#         if(len(level[-1]) < len(data)):
#             diameter+=len(level)
#         level.append(data)


#     return diameter

# 109. Convert Sorted List to Binary Search Tree

def sortedListToBST(head):
    list = getAllElements(head)
    return getNode(list, 0, len(list)-1)

    
def getNode(arr, left, right):
    mid = (left + right) // 2

    if left > right:
        return None
    Node = TreeNode(arr[mid])
    Node.left = getNode(arr, left, mid-1)
    Node.right = getNode(arr, mid+1, right)
    return Node

def getAllElements(head):
    list = []
    while(head.next!=None):
        list.append(head.data)
        head = head.next
    return list

# 104. Maximum Depth of Binary Tree
def maxDepth(root):
    if(root == None):
        return -1
    leftHeight = maxDepth(root.left) 
    rightHeight = maxDepth(root.right)
    return max(leftHeight, rightHeight) +1

def flattenBinaryTree(root):
    return

    


def check():
    tree = BinaryTree(1)
    root1 = tree.build_tree([1,2,5,3,4,"N",6])
    print(flattenBinaryTree(root1))
    tree.printTree(root1)
    # print(levelOrderTraversal(sortedListToBST([-10,-3,0,5,9])))
    # print(diameterOfBinaryTree(root1))

    # head = createLinkedList([1,2,3,4,5])
    # list= [6]
    # # head2 = createLinkedList([1,2,2,3,4,5])
    # head2 = reverseBetween(head,2,4)
    # printLinkedList(head2)
check()
