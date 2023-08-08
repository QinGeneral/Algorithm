package leetcode;

import java.util.Arrays;

class Solution75 {
    public static void main(String[] args) {
        int[] nums = new int[] { 2, 0, 2, 1, 1, 0 };
        new Solution75().sortColors(nums);
        System.out.println(Arrays.toString(nums));
    }

    public void sortColors(int[] nums) {
        int start = 0, end = nums.length - 1;
        while (start < end && nums[end] == 2) {
            end--;
        }

        while (start < end) {
            if (nums[start] == 2) {
                int tmp = nums[end];
                nums[end] = nums[start];
                nums[start] = tmp;
                while (start < end && nums[end] == 2) {
                    end--;
                }
            }
            start++;
        }
        start = 0;
        while (start < end && nums[end] == 1) {
            end--;
        }
        while (start < end) {
            if (nums[start] == 1) {
                int tmp = nums[end];
                nums[end] = nums[start];
                nums[start] = tmp;
                while (start < end && nums[end] == 1) {
                    end--;
                }
            }
            start++;
        }
    }
}