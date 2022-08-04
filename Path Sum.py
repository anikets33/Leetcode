# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            if targetSum - root.val == 0:
                return True
            else:
                return False
        
        left = right = False
        
        if root.left:
            left = self.hasPathSum(root.left, targetSum - root.val)
        if root.right:
            right = self.hasPathSum(root.right, targetSum - root.val)
            
        return left or right
