#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        fast = head
        slow = head
        temp = head

        while fast != None and fast.next != None:
            temp = slow
            fast = fast.next.next
            slow = slow.next

        temp.next = None

        left = self(head)
        right = self(slow)

        def merge(l1: Optional[ListNode], l2: Optional[listNode]):
            temp = listNode(0)
            cur = temp

            while l1 != None and l2 != None:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next

                cur = cur.next

            if l1 != None:
                cur.next = l1
            if l2 != None:
                cur.next = l2

            return temp

        return merge(left, right)


# @lc code=end
