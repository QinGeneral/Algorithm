package leetcode;

import java.util.Arrays;

class Solution283 {
    public static void main(String[] args) {
        int[] nums = new int[] { 0, 1, 0, 3, 12 };
        System.out.println(Arrays.toString(nums));
        new Solution283().moveZeroes(nums);
        System.out.println(Arrays.toString(nums));
    }

    public void moveZeroes(int[] nums) {
        int dis = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                dis++;
            } else {
                if (dis != 0) {
                    nums[i - dis] = nums[i];
                    nums[i] = 0;
                }
            }
        }
        for (int i = nums.length - dis; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}
