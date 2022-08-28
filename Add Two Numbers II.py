# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ''
        while l1:
            first += str(l1.val)
            l1 = l1.next
        second = ''
        while l2:
            second += str(l2.val)
            l2 = l2.next
        
        s = int(first) + int(second)
        
        head = tail = None
        for each in str(s):
            newNode = ListNode(int(each))
            if head:
                tail.next = newNode
                tail = tail.next
            else:
                head = tail = newNode
        
        return head
