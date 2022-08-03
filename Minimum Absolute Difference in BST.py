# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        traversal = [math.inf]
        prev = [None]
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)          
            if prev[0]:
                diff = root.val - prev[0].val
                if diff<traversal[0]:
                    traversal[0] = diff
            prev[0] = root
            inorder(root.right)
            
        inorder(root)
        
        return traversal[0]
