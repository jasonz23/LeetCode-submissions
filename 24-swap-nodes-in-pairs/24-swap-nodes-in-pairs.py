# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        a = head.val
        head.val = head.next.val
        
        head.next.val = a
        if head.next.next != None:
            
            self.swapPairs(head.next.next)
        return head
        