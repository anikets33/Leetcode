# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        tree = []
        prev = None
        m = [math.inf]
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            if prev:
                diff = prev.val - root.val
                m[0] = min(diff, m[0])
            
            prev = root
            inorder(root.right)
            
            return
            
        inorder(root, prev)
        
        return m[0]
