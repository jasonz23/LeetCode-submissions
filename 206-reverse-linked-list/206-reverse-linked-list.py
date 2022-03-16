# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None and head.next != None:
            end = head.next
            rest = self.reverseList(head.next)
            end.next = head
            head.next = None
            return rest
        return head