# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode(0)
        ret.next = head

        if not head or not head.next or not head.next.next:
            return head

        e = head
        last_even = head
        o = head.next
        first_o = head.next
        c = 0
        cur = head.next.next

        while cur:
            # print(cur.val)
            next_e = cur.next
            if c == 0:
                e.next = cur
                e = cur
                last_even = e
            elif c == 1:
                o.next = cur
                o = cur
            cur.next = None
            cur = next_e
            c = 1 - c

        o.next = None
        last_even.next = first_o

        return ret.next