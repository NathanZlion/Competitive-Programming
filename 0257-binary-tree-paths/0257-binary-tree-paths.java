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
    
    static ArrayList<String> paths = new ArrayList<String>();
    static ArrayList<Integer> currPath = new ArrayList<Integer>();
    
   /* for each value in the arraylist currpath, 
    * change values to string
    * and add them to a string then,
    * then append that to the global paths array list
    */
    public static void addPathToPaths(){
        int numberOfConnectors = currPath.size() -1;
        String pathString = "";

        for (int index = 0; index < currPath.size(); index ++){
            pathString += Integer.toString(currPath.get(index));
            if (numberOfConnectors  > 0){
                pathString += "->";
                numberOfConnectors --;
            }
        }
        paths.add(pathString);
    }

    public static void backTrack(TreeNode node){
        
        // if we've reached the leaf node
        if (node.right == null && node.left == null){
            addPathToPaths();
            return ;
        }
        
        if (node.left != null){
            // add left to paths then backtrack that
            currPath.add(node.left.val);
            backTrack(node.left);
            currPath.remove(currPath.size()-1);
        }
        
        if (node.right != null){
            // add right to paths then backtrack that
            currPath.add(node.right.val);
            backTrack(node.right);
            currPath.remove(currPath.size()-1);
        }        
    }

    public List<String> binaryTreePaths(TreeNode root) {
        TreeNode dummyNode = new TreeNode(-1);
        dummyNode.right = root;
        backTrack(dummyNode);

        // building a list from the arrayList
        String[] possiblePaths = new String[paths.size()];
        
        for (int idx = 0; idx < paths.size(); idx++){
            possiblePaths[idx] = paths.get(idx);
        }
        
        paths.clear();
        currPath.clear();

        return Arrays.asList(possiblePaths);
    }
}