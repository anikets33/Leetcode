# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        count = [0]
        
        def traverse(root, l):
            if not root:
                return
            
            temp = l.copy()
            if root.val in temp:
                temp[root.val] += 1
            else:
                temp[root.val] = 1
            if not root.left and not root.right:
                odd = 0
                for key in temp:
                    if temp[key]%2 != 0:
                        odd += 1
                if odd < 2:
                    print(l)
                    count[0] += 1

            traverse(root.left, temp)
            traverse(root.right, temp)
            
        traverse(root, {})

        return count[0]
