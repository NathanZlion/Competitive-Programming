/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    ArrayList<Integer> values = new ArrayList<Integer>();
    public void traverse(TreeNode node){
        if (node != null){
            values.add(node.val);
            traverse(node.left);
            traverse(node.right);
        }
    }
    
    public List<Integer> preorderTraversal(TreeNode root) {
        traverse(root);
        return values;
    }
}