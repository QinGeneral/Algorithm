/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    HashMap<TreeNode, Integer> map = new HashMap<>();
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        
        return Math.abs(getDepth(root.left) - getDepth(root.right)) <= 1 &&
            isBalanced(root.left) && isBalanced(root.right);
    }
    
    public int getDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int lDepth = getDepth(root.left);
        int rDepth = getDepth(root.right);
        return Math.max(lDepth, rDepth) + 1;
    }
}


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    HashMap<TreeNode, Integer> map = new HashMap<>();
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        
        getDepth(root);
        return Math.abs(getDepth(root.left) - getDepth(root.right)) <= 1 &&
            isBalanced(root.left) && isBalanced(root.right);
    }
    
    public int getDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        if (map.containsKey(root)) {
            return map.get(root);
        }
        int lDepth = getDepth(root.left);
        int rDepth = getDepth(root.right);
        map.put(root, Math.max(lDepth, rDepth) + 1);
        return map.get(root);
    }
    
    public boolean judge(TreeNode root) {
        if (root == null) {
            return true;
        }
        return Math.abs(map.get(root.left) - map.get(root.right)) <= 1 &&
            judge(root.left) && judge(root.right);
    }
}
