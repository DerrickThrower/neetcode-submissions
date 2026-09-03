# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_sum = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def helper(node):

            if node is None:
                return 0

            leftGain = max(helper(node.left),0)
            rightGain = max(helper(node.right),0)

            priceNewpath = node.val + leftGain + rightGain
            curVal = node.val + max(leftGain,rightGain)

            self.max_sum = max(self.max_sum,priceNewpath)
            return curVal


        helper(root)

        return self.max_sum

            

            


        