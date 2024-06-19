# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode(0)
        ret.next = head
        prev = ret
        while head:
            peek = head.next
            if peek and peek.val == head.val:
                delval = peek.val
                # print("delete initiate", delval)
                # print("prev ", prev.val)
                while prev.next and prev.next.val == delval:
                    prev.next = prev.next.next
                # print("prev.next.val", prev.next.val)
                head = prev.next
                # print("headval", head.val)
            else:
                prev = head
                head = head.next

        return ret.next