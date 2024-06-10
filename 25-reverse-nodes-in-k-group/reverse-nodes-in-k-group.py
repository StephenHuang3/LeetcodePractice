# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        # Dummy node
        dummy = ListNode(0)
        dummy.next = head
        retNode = dummy
        
        # Find the length of the list
        length = 0
        while head:
            length += 1
            head = head.next
        
        head = dummy.next
        prev = dummy
        
        # Reverse in k-groups      
        while length >= k:
            tail = head
            for _ in range(k - 1):
                temp = head.next
                head.next = temp.next
                temp.next = prev.next
                prev.next = temp
            
            prev = tail
            head = tail.next
            length -= k
        
        return retNode.next