package leetcode;

import java.util.Arrays;

class Solution560 {
    public static void main(String[] args) {
        int[] a = new int[] { 1, 2, 1, 2, 1 };
        System.out.println(new Solution560().subarraySum(a, 3));
    }

    public int subarraySum(int[] nums, int k) {
        if (nums.length == 0) {
            return 0;
        }
        int total = 0;

        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                if (sum == k) {
                    total++;
                }
            }
        }
        return total;
    }
}