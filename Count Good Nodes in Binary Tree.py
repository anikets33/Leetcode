# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def count(root, m):
            if not root:
                return 0
            
            c = 0
            if root.val >= m:
                m = root.val
                c = 1
            
            return count(root.left, m) + count(root.right, m) + c
    
        return count(root, -math.inf)
            
