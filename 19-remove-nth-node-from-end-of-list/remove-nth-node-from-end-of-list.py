# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenfind = head
        c = 0
        while lenfind:
            lenfind = lenfind.next
            c += 1

        # print(c)

        pos = ListNode(0)
        pos.next = head
        ret = pos

        for i in range(c - n):
            pos = pos.next

        if pos.next:
            pos.next = pos.next.next
        else:
            pos.next = None

        return ret.next