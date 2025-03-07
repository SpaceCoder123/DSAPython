from collections import deque
from OOPS.BinaryTree.TreeNode import TreeNode  # Ensure correct import

class BinaryTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def insert_left(self, parent, data):
        parent.left = TreeNode(data)

    def insert_right(self, parent, data):
        parent.right = TreeNode(data)

    def build_tree(self, values):
        if not values or values[0] == "N":
            return None

        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while i < len(values):
            current = queue.popleft()  

            # Assign the left child
            if i < len(values) and values[i] != "N":
                current.left = TreeNode(int(values[i]))
                queue.append(current.left)
            i += 1

            # Assign the right child
            if i < len(values) and values[i] != "N":
                current.right = TreeNode(int(values[i]))
                queue.append(current.right)
            i += 1

        return root

    def printTree(self, root):
        if root is None:
            return
        print(root.data)  # Fix: Use `data` instead of `value`
        self.printTree(root.left)
        self.printTree(root.right)

    def checkBalancedTree(self, root):
        def height(node):
            if node is None:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1  # Unbalanced
            return max(left_height, right_height) + 1
        
        return height(root) != -1  # True if balanced, False otherwise
