# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def checkT(a, b):
            if not a and not b:
                return True

            if not a or not b:
                return False
                    
            if a.val != b.val:
                return False
            
            return checkT(a.left, b.left) and checkT(a.right, b.right)


        def dfs(node):

            if node == None:
                return False

            if checkT(node,subRoot):
                return True

            return dfs(node.left) or dfs(node.right)
             
        return dfs(root)