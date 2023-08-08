package leetcode;

class Solution189 {
    public static void main(String[] args) {
        int[] data = new int[] { 1, 2, 3, 4, 5, 6, 7 };
        new Solution189().rotate(data, 3);
        System.out.println(java.util.Arrays.toString(data));
    }

    public void rotate(int[] nums, int k) {
        if (k == 0) {
            return;
        }
        k = k % nums.length;
        int[] tmp = new int[k];
        for (int i = nums.length - k; i < nums.length; i++) {
            tmp[i - (nums.length - k)] = nums[i];
        }

        for (int i = nums.length - k - 1; i >= 0; i--) {
            nums[i + k] = nums[i];
        }
        for (int i = 0; i < k; i++) {
            nums[i] = tmp[i];
        }
    }
}