# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if root:
            def find(root, targetSum, path=[]):

                if not root.left and not root.right:
                    if root.val == targetSum:
                        temp = []
                        temp.extend(path)
                        temp.append(root.val)
                        result.append(temp)
                        return 

                if root.left:
                    temp = []
                    temp.extend(path)
                    temp.append(root.val)
                    find(root.left, targetSum - root.val, temp)
                if root.right:
                    temp = []
                    temp.extend(path)
                    temp.append(root.val)
                    find(root.right, targetSum - root.val, temp)

                return

            find(root, targetSum)
        
        return result
