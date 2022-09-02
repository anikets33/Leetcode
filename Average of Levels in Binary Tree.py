# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        currLevel = [root]
        nextLevel = []
        res = [root.val/1]
        while currLevel:
            sumLevel = 0
            sizeLevel = 0
            while currLevel:
                t = currLevel.pop()
                if t.left:
                    nextLevel.append(t.left)
                    sumLevel += t.left.val
                    sizeLevel += 1
                if t.right:
                    nextLevel.append(t.right)
                    sumLevel += t.right.val
                    sizeLevel += 1
            currLevel, nextLevel = nextLevel, currLevel
            if sizeLevel > 0:   res.append(sumLevel/sizeLevel)
        return res
                
