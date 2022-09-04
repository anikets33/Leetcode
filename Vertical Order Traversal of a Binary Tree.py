# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}
        mini, maxi = [math.inf], [-math.inf]
        
        def markLevel(root, level, row):
            if not root:
                return 
            if level in d:
                d[level].append([root.val, row])
            else:
                d[level] = [[root.val, row]]
            mini[0] = min(level, mini[0])
            maxi[0] = max(level, maxi[0])
            markLevel(root.left, level-1, row+1)
            markLevel(root.right, level+1, row+1)
            return
        
        markLevel(root, 0, 0)
        res = []
        
        def row(i,j):
            if i[1] == j[1]:
                return -1 if i[0]<j[0] else 1
            else:
                return -1 if i[1]<j[1] else 1
        for key in d:
            d[key].sort(key = cmp_to_key(row))
        for i in range(mini[0], maxi[0]+1):
            temp = []
            for x in d[i]:
                temp.append(x[0])
            res.append(temp)
        return res
