import java.util.ArrayList;
import java.util.List;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    List<Integer> temp = new ArrayList<>();
    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> pathSum(TreeNode root, int target) {
        if (root == null) {
            return res;
        }
        preOrder(root, 0, target);
        return res;
    }

    public void preOrder(TreeNode root, int curSum, int target) {
        temp.add(root.val);
        curSum += root.val;

        if (root.left == null && root.right == null) {
            if (curSum == target) {
                res.add(new ArrayList<Integer>(temp));
            }
        }
        if (root.left != null) {
            preOrder(root.left, curSum, target);
        }
        if (root.right != null) {
            preOrder(root.right, curSum, target);
        }
        temp.remove(temp.size() - 1);
    }
}