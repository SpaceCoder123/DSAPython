from OOPS.BinaryTree.TreeNode import TreeNode
from collections import deque

class BinaryTreeProblems:

    def levelOrder(self, root):
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

    def hieghtOfATree(self, root):
        if(root == None):
            return -1
        leftHeight = self.hieghtOfATree(root.left) 
        rightHeight = self.hieghtOfATree(root.right)
        return max(leftHeight, rightHeight) +1

    def isIdentical(self, r1, r2):
        if(r1 == None and r2 == None):
            return True
        if(r1.data == r2.data):
            return self.isIdentical(r1.left, r2.left) and self.isIdentical(r1.right, r2.right)
        else:
            return False
        
    def isBalanced(self, root):
        if(root == None):
            return -1
        leftHeight = self.hieghtOfATree(root.left) 
        rightHeight = self.hieghtOfATree(root.right)
        return abs(leftHeight-rightHeight) <= 1

    def checkBalanceOptimized(self, root):
        if root is None:
            return 0
        leftHeight = self.checkBalance(root.left)
        if leftHeight == -1:
            return -1 
        
        rightHeight = self.checkBalance(root.right)
        if rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1  

    def isBalanced(self, root):
        return self.checkBalance(root) != -1

    def isSumProperty(self, root):
        if root is None:
            return True  

        if root.left is None and root.right is None:
            return True 

        leftValue = root.left.data if root.left else 0
        rightValue = root.right.data if root.right else 0

        if root.data == leftValue + rightValue:
            return self.isSumProperty(root.left) and self.isSumProperty(root.right)
        else:
            return False


    def widthOrder(self, root):
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

    def preOrder(self, root):
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

    def findfloor(self, root, inp):
        
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

    def findCeil(self, root, inp):
        
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

    def minValue(self, root):
        ##Your code here
        if(root.left != None):
            return self.minValue(root.left)
        
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

    def validateBinaryTree(self, root):

        if root is None:
            return True
        return self.ValidateBinaryTreeCalculate(root, float('-inf'), float('inf'))

    def ValidateBinaryTreeCalculate(self, root, leftLimit, rightLimit):
        if root is None:
            return True
        if leftLimit > root.data or rightLimit < root.data:
            return False
        left = self.ValidateBinaryTreeCalculate(root.left, leftLimit, root.data)
        right = self.ValidateBinaryTreeCalculate(root.right, root.data,rightLimit)
        return left and right

    def levelOrderTraversal(self, root):
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

    def rightSideView(self, root):
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

    def leftSideView(self, root):
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

    def zigzagLevelOrder(self, root):
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



    def zigZagTraversalGFG(self, root):
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

    def levelOrderTraversal(self, root):
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

    def sortedListToBST(self, head):
        list = self.getAllElements(head)
        return self.getNode(list, 0, len(list)-1)

        
    def getNode(self, arr, left, right):
        mid = (left + right) // 2

        if left > right:
            return None
        Node = TreeNode(arr[mid])
        Node.left = self.getNode(arr, left, mid-1)
        Node.right = self.getNode(arr, mid+1, right)
        return Node

    def getAllElements(self, head):
        list = []
        while(head.next!=None):
            list.append(head.data)
            head = head.next
        return list

    # 104. Maximum Depth of Binary Tree
    def maxDepth(self, root):
        if(root == None):
            return -1
        leftHeight = self.maxDepth(root.left) 
        rightHeight = self.maxDepth(root.right)
        return max(leftHeight, rightHeight) +1

    def flattenBinaryTree(self, root):
        return


    def rightSideView(self, root):
        if not root:
            return []
        
        rightViewNodes = []
        queue = [root]
        while len(queue) > 0:
            data = []
            levelSize = len(queue)
            for i in range(0, levelSize):
                node = queue.pop(0) # O(n)
                if(i == levelSize - 1): data.append(node.data)
                if (node.left is not None) : queue.append(node.left)
                if (node.right is not None) : queue.append(node.right)
        return rightViewNodes

    def right_view(self, root):
        if not root: 
            return []
        
        rightViewNodes = []
        queue = deque([root])
        
        while queue:
            queueLen = len(queue)
            for i in range(queueLen):
                node = queue.popleft() # O(1)
                if i == queueLen - 1: 
                    rightViewNodes.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                print(node.data)
        return rightViewNodes