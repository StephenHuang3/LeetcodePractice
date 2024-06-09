# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        cur = head

        while list1 and list2:
            if list1.val < list2.val:
                new = ListNode(list1.val)
                cur.next = new
                list1 = list1.next
            else:
                new = ListNode(list2.val)
                cur.next = new
                list2 = list2.next

            cur = cur.next

        while list1:
            new = ListNode(list1.val)
            cur.next = new
            list1 = list1.next
            cur = cur.next

        while list2:
            new = ListNode(list2.val)
            cur.next = new
            list2 = list2.next
            cur = cur.next

        return head.next