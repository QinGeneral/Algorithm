package leetcode;

import java.util.Comparator;
import java.util.PriorityQueue;

class Solution2 {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue<Integer>(k);
        for (int i = 0; i < nums.length; i++) {
            if (queue.size() < k) {
                queue.add(nums[i]);
            } else if (nums[i] > queue.peek()){
                queue.poll();
                queue.add(nums[i]);
            }
        }
        System.out.println(queue.size());
        return queue.poll();
    }

    public static void main(String[] args) {
        int[] nums = { 3, 2, 1, 5, 6, 4 };
        System.out.println(new Solution2().findKthLargest(nums, 2));
    }
}