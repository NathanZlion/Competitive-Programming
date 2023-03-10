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
    
    static ArrayList<Integer> levels = new ArrayList<Integer> ();

    
    public void backTrack(TreeNode node, int depth){

        if (node == null) return;
        
        if (depth == levels.size()){
            levels.add(node.val);
        } else {
           levels.set(depth, node.val);
        }

        backTrack(node.left, depth+1);
        backTrack(node.right, depth+1);
    }

    public List<Integer> rightSideView(TreeNode root) {
        levels.clear();
        backTrack(root, 0);
        List<Integer> result = levels;
        return result;
    }
}

