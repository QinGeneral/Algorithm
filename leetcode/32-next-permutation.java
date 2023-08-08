package leetcode;

import java.util.Arrays;

class Solution32 {
    public static void main(String[] args) {
        int[] nums = new int[] { 1, 2, 3 };
        new Solution32().nextPermutation(nums);
        System.out.println(Arrays.toString(nums));

        nums = new int[] { 3, 2, 1 };
        new Solution32().nextPermutation(nums);
        System.out.println(Arrays.toString(nums));

        nums = new int[] { 1, 1, 5 };
        new Solution32().nextPermutation(nums);
        System.out.println(Arrays.toString(nums));

        nums = new int[] { 1, 3, 2 };
        new Solution32().nextPermutation(nums);
        System.out.println(Arrays.toString(nums));
    }

    public void nextPermutation(int[] nums) {
        boolean isChanged = false;
        for (int i = nums.length - 1; i >= 1; i--) {
            if (nums[i] > nums[i - 1]) {
                int tmp = nums[i];
                nums[i] = nums[i - 1];
                nums[i - 1] = tmp;
                isChanged = true;
                break;
            }
        }
        if (!isChanged) {
            for (int i = 0; i < nums.length / 2; i++) {
                int tmp = nums[i];
                nums[i] = nums[nums.length - i - 1];
                nums[nums.length - i - 1] = tmp;
            }
        }
    }
}