# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # O O O O O
        # S S S N
        # F   F   F

        # O O O O O O
        # S S S S 
        # F   F   F   F

        if not head or not head.next:
            return True

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast: # odd
            slow = slow.next

        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        slow.next = None

        while head and prev:
            if head.val != prev.val:
                # print("head", head.val)
                # print("prev", prev.val)
                return False

            head = head.next
            prev = prev.next

        return True