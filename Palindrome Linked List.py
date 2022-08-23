# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast,slow = head, head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
                    
        def reverse(node):
            if not node.next:
                return node
            temp = reverse(node.next)
            node.next.next = node
            node.next = None
            return temp
            
        revHead = reverse(slow)
        
        while revHead:
            if revHead.val != head.val:
                return False
            revHead = revHead.next
            head = head.next
        
        return True 
'''
def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            
            temp = rev
            rev = slow
            slow = slow.next
            rev.next = temp
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
'''
'''
def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        s, rs = '', ''
        while head:
            s += str(head.val)
            rs = str(head.val) + rs
            head = head.next
        return s == rs
'''
