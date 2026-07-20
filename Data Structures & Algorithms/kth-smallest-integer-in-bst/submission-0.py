# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        result = [None]
        def inorder(node):
            if node is None:
                return

            
            inorder(node.left)

            count[0] += 1
            if count[0] == k:
                result[0] = node.val
                

            inorder(node.right)

            
        inorder(root)

        if result[0] is None:
            raise ValueError(f"k={k} is out of range for the given BST")

        return result[0]