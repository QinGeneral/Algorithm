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
    List<String> res = new ArrayList<String>();
    public List<String> binaryTreePaths(TreeNode root) {
        if (root == null) {
            return res;
        }
        preOrder(root, "");
        return res;
    }

    public void preOrder(TreeNode root, String str) {
        str += "->" + root.val;
        if (root.left != null) {
            preOrder(root.left, str);
        }
        if (root.right != null) {
            preOrder(root.right, str);
        }
        if (root.left == null && root.right == null) {
            res.add(str.substring(2));
        }
    }
}