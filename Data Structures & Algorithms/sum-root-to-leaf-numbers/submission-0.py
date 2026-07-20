# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node,count):

            if not node:
                return 0

            count = count * 10 + node.val

            if not node.left and not node.right:
                return count

            left = dfs(node.left,count)
            right = dfs(node.right, count)

            return left + right











        return dfs(root,0)
        