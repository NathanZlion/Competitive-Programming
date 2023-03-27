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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null){
            return head;
        }
        
        // find length and make circular
        
        int listLength = 0;
        ListNode dummyNode = new ListNode(-1, head);
        
        ListNode curr = dummyNode;
        
        while (curr.next != null){
            listLength += 1;
            curr = curr.next;
        }
        
        // making circular linked list
        curr.next = head;

        int distanceToHead =  listLength - (k % listLength);
        curr = dummyNode;

        for (int index = 0; index < distanceToHead; index ++){
            curr = curr.next;
        }
        
        ListNode res = curr.next;
        curr.next = null;
        return res;        
        
    }
}