# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        
        def preorder(root):
            
            if not root:
                return root
            stack.append(root)
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)
                
        preorder(root)
        
        while stack:
            node = stack.pop(0)
            node.left = None
            if stack:
                node.right = stack[0]
            else:
                node.right = None
            
            
            
        
        
        
        
                
            
