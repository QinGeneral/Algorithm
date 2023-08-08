package leetcode;

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution239 {
    public static void main(String[] args) {
        int[] data = new int[] { 1, 3, -1, -3, 5, 3, 6, 7 };
        System.out.println(Arrays.toString(new Solution239().maxSlidingWindow(data, 3)));
    }

    public int[] maxSlidingWindow(int[] nums, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue<>(k);
        for (int i = 0; i < k; i++) {
            queue.add(-nums[i]);
        }
        int[] result = new int[nums.length - k + 1];
        for (int i = k; i < nums.length; i++) {
            System.out.println(queue);
            result[i - k] = -queue.peek();
            queue.remove(-nums[i - k]);
            queue.add(-nums[i]);
        }
        result[nums.length - k] = -queue.peek();
        return result;
    }
}
