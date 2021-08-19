import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        boolean isReverse = false;
        while (queue.size() > 0) {
            List<Integer> temp = new ArrayList<>();

            int size = queue.size();
            while (size > 0) {
                TreeNode node = queue.poll();
                if (isReverse) {
                    temp.add(0, node.val);
                } else {
                    temp.add(node.val); 
                }
                if (node.left != null) {
                    queue.add(node.left);
                }
                if (node.right != null) {
                    queue.add(node.right);
                }
                size--;
            }
            isReverse = !isReverse;
            result.add(temp);
        }
        return result;
    }
}