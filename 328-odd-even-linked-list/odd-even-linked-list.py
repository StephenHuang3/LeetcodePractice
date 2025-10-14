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
        o = head.next
        first_o = o

        while o and o.next:
            e.next = o.next
            e = e.next
            o.next = e.next
            o = o.next

        if o:
            o.next = None
        e.next = first_o

        return ret.next