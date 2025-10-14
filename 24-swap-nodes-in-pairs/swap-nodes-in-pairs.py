# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        ret = ListNode(0)
        prev = ret
        ret.next = head
        cur = head

        while cur and cur.next:
            next_iter = cur.next.next
            next_prev = cur
            n1 = cur
            n2 = cur.next
            prev.next = n2
            n2.next = n1
            n1.next = next_iter
            cur = next_iter
            prev = next_prev

        return ret.next


        