# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        a = str(root.val)
        b = self.tree2str(root.left)
        c = self.tree2str(root.right)
        
        if len(b) == 0 and len(c) == 0:
            return a
        elif len(c) == 0:
            return a + '(' + b + ')'
        else:
            return a + '(' + b + ')' + '(' + c + ')'
        
