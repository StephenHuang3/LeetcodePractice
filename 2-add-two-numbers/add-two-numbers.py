# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode(0)
        cur = ret
        carry = 0
        while l1 and l2:
            comb = l2.val + l1.val + carry
            new = ListNode(comb % 10)
            cur.next = new
            cur = cur.next
            carry = comb // 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            new = ListNode((carry + l1.val) % 10)
            cur.next = new
            cur = cur.next
            carry = (carry + l1.val) // 10
            l1 = l1.next

        while l2:
            new = ListNode((carry + l2.val) % 10)
            cur.next = new
            cur = cur.next
            carry = (carry + l2.val) // 10
            l2 = l2.next

        if carry != 0:
            new = ListNode(1)
            cur.next = new


        return ret.next


        