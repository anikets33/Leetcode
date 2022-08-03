# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder(self, root, traversal):
        if not root:    return None
        
        if root.left:   self.inorder(root.left, traversal)
        traversal.append(root.val)
        if root.right:  self.inorder(root.right, traversal)
        
        return traversal
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        return self.inorder(root, [])
