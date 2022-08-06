# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s = [0]
        
        def leaf(root, child):
            if not root.left and not root.right:
                if child == 1:
                    s[0] += root.val
                return
            
            if root.left:
                leaf(root.left, 1)
            if root.right:
                leaf(root.right, 0)
            
            return
        
        leaf(root, 0)
        
        return s[0]
