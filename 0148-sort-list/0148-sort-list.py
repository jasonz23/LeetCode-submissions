# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        if (len(l) ==0):
            return None
        l = sorted(l)
        
        h = ListNode();
        t = h
        for index,num in enumerate(l):
            t.val = num
            if (index + 1 < len(l)):
                f = ListNode()
                t.next = f
                t = t.next
        return h
            
        