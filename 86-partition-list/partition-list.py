# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ret = ListNode(0)
        ret.next = head
        prev = ret
        less = ret
        foundLarger = False
        
        while head:
            if head.val < x and foundLarger:
                prev.next = head.next
                temp = less.next
                less.next = head
                head.next = temp
                less = head
                head = prev.next
            elif head.val < x and not foundLarger:
                if less:
                    less = less.next
                prev = head
                head = head.next
            else:
                prev = head
                head = head.next
                foundLarger = True


        return ret.next