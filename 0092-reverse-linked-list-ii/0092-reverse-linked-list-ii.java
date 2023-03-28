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
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        // find the left
        // find the right
        // reverse what's in between
        // return the head
        
        ListNode dummyHead = new ListNode(-1, head);
        
        ListNode curr = dummyHead;
        
        for (int count = 1; count < left; count++){
            curr = curr.next;
        }
        ListNode start = curr;
        ListNode reverseStart = start.next;
        
        int leftToRight = right - left + 1;

        for (int count = 0; count < leftToRight ; count++){
            curr = curr.next;
        }
        
        ListNode reverseEnd = curr;
        ListNode end = reverseEnd.next;
        
        // reverse what's between reverseStart and reverseEnd
        reverseEnd.next = null;
        ListNode dummy = new ListNode(-2, reverseStart);
        ListNode prev = dummy;
        curr = dummy.next;
        ListNode next = curr.next;
        
        while (curr != null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        
        start.next = reverseEnd;
        reverseStart.next = end;
        return dummyHead.next;
        
    }
}