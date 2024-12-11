# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        cur = slow.next
        slow.next = None
        
        while cur:
            fut = cur.next
            cur.next = prev
            prev = cur
            cur = fut

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
            
        return head
        # if prev:
        #     new.next = prev
        # if head:
        #     new.next = head

        return ret.next
