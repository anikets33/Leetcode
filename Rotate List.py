# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        tail = head
        c = 1
        
        while tail.next:
            tail = tail.next
            c += 1
        
        tail.next = head
        if c>=k:
            k = c-k
        else:
            k = c-k + c*(k//c)
        
        for i in range(k):
            tail = tail.next
        
        head = tail.next
        tail.next = None
        
        return head
        
        
