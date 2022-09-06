# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def prune(root):
            if not root:
                return False
            
            a = prune(root.left)
            b = prune(root.right)
            
            if not a:
                root.left = None
            if not b:
                root.right = None
            
            return a or b or root.val==1
        
        t = prune(root)
        if not t:
            root = None
        
        return root
