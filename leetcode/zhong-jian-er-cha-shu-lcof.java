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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0) {
            return null;
        }
        return buildTree(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);
    }

    public TreeNode buildTree(int[] preorder, int pStart, int pEnd, int[] inorder, int iStart, int iEnd) {
        if (pStart > pEnd) {
            return null;
        }
        if (pStart == pEnd) {
            return new TreeNode(preorder[pStart]);
        }
        TreeNode root = new TreeNode(preorder[pStart]);
        int i = iStart;
        for (; i <= iEnd; i++) {
            if (inorder[i] == preorder[pStart]) {
                break;
            }
        }
        root.left = buildTree(preorder, pStart + 1, pStart + i - iStart, inorder, iStart, i - 1);
        root.right = buildTree(preorder, pStart + i - iStart + 1, pEnd, inorder, i + 1, iEnd);
        return root;
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
    HashMap<Integer, Integer> indexMap = new HashMap<>();
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0) {
            return null;
        }
        for (int i = 0; i < inorder.length; i++) {
            indexMap.put(inorder[i], i);
        }
        return buildTree(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);
    }

    public TreeNode buildTree(int[] preorder, int pStart, int pEnd, int[] inorder, int iStart, int iEnd) {
        if (pStart > pEnd) {
            return null;
        }
        if (pStart == pEnd) {
            return new TreeNode(preorder[pStart]);
        }
        TreeNode root = new TreeNode(preorder[pStart]);
        int i = indexMap.get(root.val);
        root.left = buildTree(preorder, pStart + 1, pStart + i - iStart, inorder, iStart, i - 1);
        root.right = buildTree(preorder, pStart + i - iStart + 1, pEnd, inorder, i + 1, iEnd);
        return root;
    }
}