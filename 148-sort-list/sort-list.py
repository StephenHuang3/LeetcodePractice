# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1, l2):
            ret = ListNode(0)
            cur = ret
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next

            if l1:
                cur.next = l1
            if l2:
                cur.next = l2

            # print("ret", ret)
            # print("l1", l1)
            # print("l2", l2)
            return ret.next

        def mergesort(lis):
            if not lis or not lis.next:
                return lis
            
            slow = lis
            fast = lis
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            prev.next = None
            l1 = mergesort(lis)
            l2 = mergesort(slow)
            # print("l1", l1)
            # print("l2", l2)
            return merge(l1, l2)

        return mergesort(head)

                
