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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        getPath(root, p, list1);
        getPath(root, q, list2);
        int i = 0, j = 0;
        TreeNode lastNode = null;
        while (i < list1.size() && j < list2.size()) {
            if (list1.get(i) == list2.get(j)) {
                lastNode = list1.get(i);
            }
            i++;
            j++;
        }
        return lastNode;
    }

    ArrayList<TreeNode> list1 = new ArrayList<>();
    ArrayList<TreeNode> list2 = new ArrayList<>();
    public boolean getPath(TreeNode root, TreeNode target, ArrayList<TreeNode> list) {
        if (root == null) {
            return false;
        }
        list.add(root);
        if (root == target) {
            return true;
        }
        if (getPath(root.left, target, list) || getPath(root.right, target, list)) {
            return true;
        }
        list.remove(list.size() - 1);
        return false;
    }
}