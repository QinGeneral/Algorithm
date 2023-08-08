package leetcode;

import java.util.Arrays;

class Solution53 {
    public static void main(String[] args) {
        System.out.println(new Solution53().maxSubArray(new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 }));
    }

    public int maxSubArray(int[] nums) {
        int max = nums[0];

        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
            System.out.println(i + " " + Arrays.toString(dp));
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}