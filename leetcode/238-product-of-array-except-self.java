package leetcode;

class Solution238 {
    public static void main(String[] args) {
        int[] data = new int[] { 1, 2, 3, 4 };
        System.out.println(java.util.Arrays.toString(new Solution238().productExceptSelf(data)));
        data = new int[] { -1, 1, 0, -3, 3 };
        System.out.println(java.util.Arrays.toString(new Solution238().productExceptSelf(data)));
    }

    public int[] productExceptSelf(int[] nums) {
        int[] L = new int[nums.length];
        int[] R = new int[nums.length];

        L[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            L[i] = L[i - 1] * nums[i - 1];
        }

        R[nums.length - 1] = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            R[i] = R[i + 1] * nums[i + 1];
        }
        int[] result = new int[nums.length];
        for (int i = 0; i < result.length; i++) {
            result[i] = L[i] * R[i];
        }
        return result;
    }

    public int[] productExceptSelf2(int[] nums) {
        int[] result = new int[nums.length];
        result[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }

        int R = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            R = R * nums[i + 1];
            result[i] = result[i] * R;
        }
        return result;
    }
}