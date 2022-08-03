# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = []
        
        def lca(root, p, q):
            if not root:
                return [False, False]
            
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)
            
            local = [False, False]
            if root == p:
                local[0] = True
            elif root == q:
                local[1] = True
            
            l = local[0] or left[0] or right[0]
            r = local[1] or left[1] or right[1]
            
            if l and r:
                result.append(root)
                return [False, False]
            else:
                return [l, r]
        
        lca(root, p, q)
        return result[0]
