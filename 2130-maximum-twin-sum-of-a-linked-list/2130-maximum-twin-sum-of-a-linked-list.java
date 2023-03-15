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
    public int pairSum(ListNode head) {
        
        ListNode slow = head;
        ListNode fast = head.next;
        
        ArrayList<Integer> stack = new ArrayList<Integer>(0);
        
        while (fast != null){
            stack.add(slow.val);
            
            slow = slow.next;
            fast = fast.next;

            if (fast != null) fast = fast.next;
        }
        
        int maxSum = 0;

        while (slow != null){
            maxSum = Math.max(maxSum, slow.val + stack.remove(stack.size()-1));
            slow = slow.next;
        }
        

        return maxSum;
        
    }
}




