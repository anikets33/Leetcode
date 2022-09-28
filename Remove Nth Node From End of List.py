# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        
        k = length - n
        if k == 0:
            return head.next
        
        temp = head
        for i in range(k-1):
            temp = temp.next
        
        temp.next = temp.next.next
        
        return head
