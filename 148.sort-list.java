/*
 * @lc app=leetcode id=148 lang=java
 *
 * [148] Sort List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
public ListNode sortList(ListNode head) {
    return mergeSort(head);
}

public ListNode mergeSort(ListNode head){
    if(head == null || head.next == null){
        return head;
    }
    ListNode l = head;
    ListNode r = head;
    ListNode temp = head;
    while(r != null && r.next != null){
        temp = l;
        l = l.next;
        r = r.next.next;
    }
    temp.next = null;
    ListNode leftP = mergeSort(head);
    ListNode rightP = mergeSort(l);
    return merge(leftP, rightP);
}

public ListNode merge(ListNode l, ListNode r){
    ListNode dummy = new ListNode(-1);
    ListNode current = dummy;
    while(l != null && r != null){
        if(l.val > r.val){
            current.next = r;
            r = r.next;
        }else{
            current.next = l;
            l = l.next;
        }
        current = current.next;
    }

    if(l != null){
        current.next = l;
    }
    if(r != null){
        current.next = r;
    }
    return dummy.next;
}
// @lc code=end
