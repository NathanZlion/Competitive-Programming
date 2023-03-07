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
            traverse(node.left);
            values.add(node.val);
            traverse(node.right);
        }
    }
    
    public List<Integer> inorderTraversal(TreeNode root) {
        traverse(root);
        return values;
    }
}