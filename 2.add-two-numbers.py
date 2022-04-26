#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=head=ListNode()
        carry = 0
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            if (carry != 0):
                sum += carry
            
            if sum > 9:
                sum = sum % 10
                carry = 1
            else:
                carry = 0
                
            l3.next = ListNode(sum)
            l3=l3.next
        if carry:
            l3.next=ListNode(1)
        return head.next
# @lc code=end

