# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxDiameter =[0]
        
        def diameter(root):
            
            if not root:
                return 0
            
            left = diameter(root.left)
            right = diameter(root.right)
            
            maxDiameter[0] = max(maxDiameter[0], left+right+1)
            
            return max(left, right) + 1
        
        height = diameter(root)
        
        return maxDiameter[0] - 1
