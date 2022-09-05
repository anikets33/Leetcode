"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:    return []
        currLevel = [root]
        nextLevel = []
        res = [[root.val]]
        while currLevel:
            currValues = []
            while currLevel:
                node = currLevel.pop(0)
                for each in node.children:
                    nextLevel.append(each)
                    currValues.append(each.val)
            if currValues:  res.append(currValues)
            currLevel, nextLevel = nextLevel, currLevel
        return res
