# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumNumbers(self, root):
        def dfs(node, current):
            if not node:
                return 0
            
            # Build number
            current = current * 10 + node.val
            
            # If leaf node → return the number
            if not node.left and not node.right:
                return current
            
            # Recurse left + right
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)

