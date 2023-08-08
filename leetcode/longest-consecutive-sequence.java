package leetcode;

import java.util.HashSet;

class Solution49 {

    public static void main(String[] args) {
        int[] nums = new int[] { 100, 4, 200, 1, 3, 2 };
        System.out.println(new Solution49().longestConsecutive(nums));

        int[] nums2 = new int[] { 0, 3, 7, 2, 5, 8, 4, 6, 0, 1 };
        System.out.println(new Solution49().longestConsecutive(nums2));

        int[] nums3 = new int[] { 9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6 };
        System.out.println(new Solution49().longestConsecutive(nums3));
    }

    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        HashSet<Integer> set = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }

        int max = 1;
        int cur = 1;

        for (int i = 0; i < nums.length; i++) {
            if (set.contains(nums[i] - 1)) {
                continue;
            }
            while (set.contains(nums[i] + cur)) {
                cur++;
            }
            if (cur > max) {
                max = cur;
            }
            cur = 1;
        }
        return max;
    }
}