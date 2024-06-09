# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        lnodeprev = prev
        lnode = prev.next
        cur = lnode
        oldprev = None

        for _ in range(right - left + 1):
            next_temp = cur.next
            cur.next = oldprev
            oldprev = cur
            cur = next_temp

        lnodeprev.next = oldprev
        lnode.next = cur

        return dummy.next