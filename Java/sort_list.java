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

// Using merge sort
class Solution {
    
    // merge two sorted lists and return the head
    public ListNode merge(ListNode head1, ListNode head2) {
        
        if (head1 == null) {
            return head2;
        }
        
        if (head2 == null) {
            return head1;
        }
        
        if (head1.val < head2.val) {
            head1.next = merge(head1.next, head2);
            return head1;
        }
        else {
            head2.next = merge(head1, head2.next);
            return head2;
        }
        
        
    }
    
    public ListNode sortList(ListNode head) {
        
        if (head == null || head.next == null) {
            return head;
        }
        
        // use fast and slow pointer to get to the middle of the linked list and then divide
        ListNode prev = head;
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        prev.next = null; // split the list in half and then keep dividing and then merge them after sorting individual nodes
        ListNode head1 = sortList(head);
        ListNode head2 = sortList(slow);
        
        return merge(head1, head2);
        
    }
}
