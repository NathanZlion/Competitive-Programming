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
    
    int totalSum = 0;
    int pathSum = 0;
    
    public int sumNumbers(TreeNode root) {
        
        dfs(root);
        return totalSum;
        
    }
    
    
    public void dfs(TreeNode node){
        pathSum *= 10;
        pathSum += node.val;

        if (node.left != null){
            dfs(node.left);
        }
        if (node.right != null){
            dfs(node.right);
        }
        
        if (node.left == null & node.right == null){
            totalSum += pathSum;
        }

        pathSum -= node.val;
        pathSum /= 10;
    }
}







