#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = head = ListNode(0)
        curpos1 = list1
        curpos2 = list2

        while curpos1 != None and curpos2 != None:
            if curpos1.val < curpos2.val:
                cur.next = curpos1
                curpos1 = curpos1.next
                cur = cur.next
            else:
                cur.next = curpos2
                curpos2 = curpos2.next
                cur = cur.next

        if curpos1 != None:
            cur.next = curpos1

        if curpos2 != None:
            cur.next = curpos2

        return head.next


# @lc code=end
