#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        retHead = head
        len = 1;
        
        while(head.next != None):
            len += 1
            head = head.next
        
        head = retHead
    
        for x in range(len - n - 1):
            head = head.next
        
        if(len - n == 0):
            return head.next
        
        head.next = head.next.next

        return retHead

        
# @lc code=end

