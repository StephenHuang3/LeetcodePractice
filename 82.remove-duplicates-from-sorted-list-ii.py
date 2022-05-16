#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        h = ListNode(101)
        h.next = head
        curr = h
        root = h.next
        prev = None

        while root != None:
            if curr.val != root.val:
                prev = curr
                curr = root
                root = root.next
            else:
                while root != None and curr.val == root.val:
                    curr.next = root.next
                    root = root.next
                prev.next = root
                curr = prev

        return h.next


# @lc code=end
