#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        retHead = head
        prevHead = head
        lastSwap = head

        first = True

        if(head.next == None):
            return retHead

        head = head.next

        while True:
            prevHead.next = head.next
            head.next = prevHead

            if first:
                retHead = head
                first = False
            

            if (first == False):
                lastSwap.next = head

            head = head.next



            lastSwap = head
            

            if(head.next.next != None):
                head = head.next.next
                prevHead = prevHead.next
            else:
                return retHead

        return retHead
# @lc code=end

