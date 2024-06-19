# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        c = 0
        flen = head
        end = flen
        while flen:
            c += 1
            end = flen
            flen = flen.next

        if k % c == 0:
            return head
        
        pos = head
        for i in range(c - k % c - 1):
            pos = pos.next

        start = pos.next
        pos.next = None
        end.next = head
        return start
