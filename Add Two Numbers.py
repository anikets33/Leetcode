# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        first, second = l1, l2
        carry = 0
        head = tail = None
        
        while first or second:
            
            s = (first.val if first else 0) + (second.val if second else 0) + carry
            carry = 1 if s>=10 else 0
            
            newNode = ListNode(s%10)
            if not head:
                head = tail = newNode
            else:
                tail.next = newNode
                tail = newNode
            
            if first:
                first = first.next
            if second:
                second = second.next
                
        if carry == 1:
            newNode = ListNode(1)
            tail.next = newNode
            tail = newNode
        
        return head
