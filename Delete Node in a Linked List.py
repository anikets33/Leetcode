# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        t = node
        prev = None
        while t.next:
            t.val, t.next.val = t.next.val, t.val
            prev = t
            t = t.next
        prev.next = None
